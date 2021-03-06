disabled = False
try:
    # pyglet requires ctypes > 1.0.0
    import ctypes
    ctypes_major = int(ctypes.__version__.split('.')[0])
    if ctypes_major < 1:
        disabled = True
except ImportError:
    disabled = True

try:
    # if pyglet.gl fails to import, e.g. opengl is missing, we disable the tests
    import pyglet.gl
    import pyglet.window
except ImportError:
    disabled = True

def setup_module(module):
    """py.test support"""
    if module.disabled:
        import pytest
        pytest.skip("Pyglet and/or OpenGL are unavailable.")

from sympy import symbols, sin, cos
x, y, z = symbols('x, y, z')

def test_import():
    from sympy import Plot

def test_plot_2d():
    from sympy import Plot
    p = Plot(x, [x, -5, 5, 4], visible=False)
    p.wait_for_calculations()

def test_plot_2d_discontinuous():
    from sympy import Plot
    p = Plot(1/x, [x, -1, 1, 2], visible=False)
    p.wait_for_calculations()

def test_plot_3d():
    from sympy import Plot
    p = Plot(x*y, [x, -5, 5, 5], [y, -5, 5, 5], visible=False)
    p.wait_for_calculations()

def test_plot_3d_discontinuous():
    from sympy import Plot
    p = Plot(1/x, [x, -3, 3, 6], [y, -1, 1, 1], visible=False)
    p.wait_for_calculations()

def test_plot_2d_polar():
    from sympy import Plot
    p = Plot(1/x, [x,-1,1,4], 'mode=polar', visible=False)
    p.wait_for_calculations()

def test_plot_3d_cylinder():
    from sympy import Plot
    p = Plot(1/y, [x,0,6.282,4], [y,-1,1,4], 'mode=polar;style=solid',
             visible=False)
    p.wait_for_calculations()

def test_plot_3d_spherical():
    from sympy import Plot
    p = Plot(1, [x,0,6.282,4], [y,0,3.141,4], 'mode=spherical;style=wireframe',
             visible=False)
    p.wait_for_calculations()

def test_plot_2d_parametric():
    from sympy import Plot
    p = Plot(sin(x), cos(x), [x, 0, 6.282, 4], visible=False)
    p.wait_for_calculations()

def test_plot_3d_parametric():
    from sympy import Plot
    p = Plot(sin(x), cos(x), x/5.0, [x, 0, 6.282, 4], visible=False)
    p.wait_for_calculations()

def _test_plot_log():
    from sympy import Plot
    p = Plot(log(x), [x,0,6.282,4], 'mode=polar', visible=False)
    p.wait_for_calculations()

def test_plot_integral():
    # Make sure it doesn't treat x as an independent variable
    from sympy import Plot, Integral
    p = Plot(Integral(z*x, (x, 1, z), (z, 1, y)), visible=False)
    p.wait_for_calculations()
