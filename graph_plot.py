import chainer.training.trigger as trigger_module
from chainer.training import extension
import matplotlib
from os import path

matplotlib.use('Agg')
from matplotlib import pyplot as plot
import numpy as np


class GlaphPlot(extension.Extension):
    def __init__(self, y_keys, x_key='iteration', trigger=(1, 'epoch'), xlim=None, ylim=None, file_name='graph.png'):

        self._x_key = x_key
        if isinstance(y_keys, str):
            y_keys = (y_keys,)

        self._y_keys = y_keys
        self._summary = {y_key: [] for y_key in y_keys}
        self._xlim = xlim
        self._ylim = ylim
        self._trigger = trigger_module.get_trigger(trigger)
        self._file_name = file_name

    def __call__(self, trainer):
        # accumulate the observations
        observation = trainer.observation
        summary = self._summary

        updater = trainer.updater
        observation['epoch'] = updater.epoch
        observation['iteration'] = updater.iteration

        if self._x_key in observation:
            x = observation[self._x_key]

            for y_key in summary.keys():
                if y_key in observation:
                    summary[y_key].append((x, observation[y_key]))

        if self._trigger(trainer):
            # output the result
            f = plot.figure()
            a = f.add_subplot(111)
            a.set_xlabel(self._x_key)

            if self._xlim is not None:
                a.set_xlim(self._xlim)

            if self._ylim is not None:
                a.set_ylim(self._ylim)

            flag_any_item = False
            for y_key in self._y_keys:
                xy = summary[y_key]
                if len(xy) == 0:
                    continue

                flag_any_item = True
                xy = np.array(xy)
                a.plot(xy[:, 0], xy[:, 1], label=y_key)

            if flag_any_item:
                a.legend(loc='best')
                f.savefig(path.join(trainer.out, self._file_name))

            plot.close()
