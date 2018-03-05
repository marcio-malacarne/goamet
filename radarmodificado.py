#Adaptado do codigo disponivel em https://gist.githubusercontent.com/sergiobuj/6721187/raw/67661d05f14a0659b118874c59e9b3aaba7bf378/radar.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection

def _radar_factory(num_vars):
    theta = 2*np.pi * np.linspace(0, 1-1./num_vars, num_vars)
    theta += np.pi/2

    def unit_poly_verts(theta):
        x0, y0, r = [0.5] * 3
        verts = [(r*np.cos(t) + x0, r*np.sin(t) + y0) for t in theta]
        return verts

    class RadarAxes(PolarAxes):
        name = 'radar'
        RESOLUTION = 1

        def fill(self, *args, **kwargs):
            closed = kwargs.pop('closed', True)
            return super(RadarAxes, self).fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            lines = super(RadarAxes, self).plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(theta * 180/np.pi, labels)

        def _gen_axes_patch(self):
            verts = unit_poly_verts(theta)
            return plt.Polygon(verts, closed=True, edgecolor='k')

        def _gen_axes_spines(self):
            spine_type = 'circle'
            verts = unit_poly_verts(theta)
            verts.append(verts[0])
            path = Path(verts)
            spine = Spine(self, spine_type, path)
            spine.set_transform(self.transAxes)
            return {'polar': spine}

    register_projection(RadarAxes)
    return theta

def radar_graph(labels = [],valores0=[], valores1 = [], valores2=[],valores3=[],valores4=[],valores5=[],valores6=[],valores7=[],valores8=[],valores9=[],valores10=[],valores11=[],valores12=[]):
    N = len(labels) 
    theta = _radar_factory(N)
    max_val = max(max(valores0),max(valores1),max(valores2),max(valores3),max(valores4),max(valores5),max(valores6),max(valores7),max(valores8),max(valores9),max(valores10),max(valores11),max(valores12))
    fig = plt.figure(figsize=(11.5,8))
    ax = fig.add_subplot(1, 1, 1, projection='radar')
    ax.plot(theta, valores0, color='chartreuse')
    ax.plot(theta, valores1, color='r')
    ax.plot(theta, valores2, color='b')
    ax.plot(theta, valores3, color='g')
    ax.plot(theta, valores4, color='c')
    ax.plot(theta, valores5, color='m')
    ax.plot(theta, valores6, color='y')
    ax.plot(theta, valores7, color='darkcyan')
    ax.plot(theta, valores8, color='royalblue')
    ax.plot(theta, valores9, color='lime')
    ax.plot(theta, valores10, color="#248860")
    ax.plot(theta, valores11, color='olive')
    ax.plot(theta, valores12, color='tomato')
    ax.set_varlabels(labels)
    #plt.show()
    

