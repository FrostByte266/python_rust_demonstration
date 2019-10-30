use ndarray::{ArrayViewD, Array, Array1, Array2, arr2};
use numpy::{PyArrayDyn, IntoPyArray};
use pyo3::prelude::{pymodule, PyModule, PyResult, Python};
use pyo3::types::{PyTuple};
use core::f64::consts::PI;

#[pymodule]
fn rustic(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    fn make_triangle(x_origin: f64, y_origin: f64, w: f64, h: f64, r: bool) -> (Array2<f64>, Array2<f64>) {
        let x;
        let y;
        if r {
            x = arr2(&[
                [x_origin],
                [x_origin],
                [x_origin + w]
            ]);
            y = arr2(&[
                [y_origin],
                [y_origin + h],
                [y_origin]
            ]);
        } else {
            x = arr2(&[
                [x_origin],
                [(x_origin + w) / 2.],
                [(x_origin + w)]
            ]);
            y = arr2(&[
                [y_origin],
                [h],
                [y_origin]
            ]);
        }

        (x, y)
    }

    #[pyfn(m, "make_triangle")]
    fn make_triangle_py(_py: Python, x_origin: f64, y_origin: f64, w: f64, h: f64, r: bool) -> &PyTuple {
        let res = make_triangle(x_origin, y_origin, w, h, r);
        let x = res.0.into_pyarray(_py).to_owned();
        let y = res.1.into_pyarray(_py).to_owned();
        PyTuple::new(_py, &[x, y])
    }

    fn get_angle(a: ArrayViewD<'_, f64>, b: ArrayViewD<'_, f64>, c: ArrayViewD<'_, f64>) -> PyResult<f64> {
        let c1b1 = c[1] - b[1];
        let c0b0 = c[0] - b[0];
        let a1b1 = a[1] - b[1];
        let a0b0 = a[0] - b[0];

        Ok(((c1b1.atan2(c0b0) - a1b1.atan2(a0b0)).to_degrees()).abs())
    }

    #[pyfn(m, "get_angle")]
    fn get_angle_py(
        _py: Python<'_>,
        a: &PyArrayDyn<f64>,
        b: &PyArrayDyn<f64>,
        c: &PyArrayDyn<f64>
    ) -> PyResult<f64> {
        let a = a.as_array();
        let b = b.as_array();
        let c = c.as_array();
        get_angle(a, b, c)
    }

    fn find_distance(a: ArrayViewD<'_, f64>, b: ArrayViewD<'_, f64>) -> PyResult<f64> {
        let y_diff = b[1] - a[1];
        let x_diff = b[0] - a[0];

        let y_diff_squared = y_diff.powi(2);
        let x_diff_squared = x_diff.powi(2);

        let sum_square_diff = y_diff_squared + x_diff_squared;

        Ok(sum_square_diff.sqrt())
    }

    #[pyfn(m, "find_distance")]
    fn find_distance_py(
        _py: Python<'_>,
        a: &PyArrayDyn<f64>,
        b: &PyArrayDyn<f64>
    ) -> PyResult<f64> {
        let a = a.as_array();
        let b = b.as_array();
        find_distance(a, b)
    }

    fn circle_points(r: f64) -> (Array1<f64>, Array1<f64>) {
        let mut x = Array::linspace(0., PI*2., 100);
        let mut y = x.clone();

        for i in 0..x.len() {
            let iter_x = x[i] as f64;
            let iter_y = y[i] as f64;
            x[i] = r * iter_x.cos();
            y[i] = r * iter_y.sin();
        }

        (x, y)
    }

    #[pyfn(m, "circle_points")]
    fn circle_points_py(_py: Python, r: f64) -> &PyTuple {
        let res = circle_points(r);
        let x = res.0.into_pyarray(_py).to_owned();
        let y = res.1.into_pyarray(_py).to_owned();
        PyTuple::new(_py, &[x, y])
    }

    fn circle_points_offset(r: f64, x_off: f64, y_off: f64) -> (Array1<f64>, Array1<f64>) {
        let mut x = Array::linspace(0., PI*2., 100);
        let mut y = x.clone();

        for i in 0..x.len() {
            let iter_x = x[i] as f64;
            let iter_y = y[i] as f64;
            x[i] = r * iter_x.cos() + x_off;
            y[i] = r * iter_y.sin() + y_off;
        }

        (x, y)
    }

    #[pyfn(m, "circle_points_offset")]
    fn circle_points_offset_py(_py: Python, r: f64, x_off: f64, y_off: f64) -> &PyTuple {
        let res = circle_points_offset(r, x_off, y_off);
        let x = res.0.into_pyarray(_py).to_owned();
        let y = res.1.into_pyarray(_py).to_owned();
        PyTuple::new(_py, &[x, y])
    }

    Ok(())
}