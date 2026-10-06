"""Offline checks of numerical examples in the 90 knowledge frameworks.
Run with Python 3.10+: python docs/learning/knowledge/verify_examples.py
This checks authored examples, not learner mastery or model quality.
"""
from __future__ import annotations
import math
import unittest


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    if not a or not b or not a[0] or not b[0]:
        raise ValueError('Matrices must be nonempty.')
    if any(len(r) != len(a[0]) for r in a) or any(len(r) != len(b[0]) for r in b):
        raise ValueError('Ragged matrix.')
    if len(a[0]) != len(b):
        raise ValueError('Inner dimensions do not match.')
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def softmax(xs: list[float]) -> list[float]:
    if not xs or not all(math.isfinite(x) for x in xs):
        raise ValueError('This teaching helper requires finite nonempty scores.')
    top = max(xs)
    es = [math.exp(x - top) for x in xs]
    total = sum(es)
    return [e / total for e in es]


class KnowledgeExamples(unittest.TestCase):
    def close(self, actual: list[float], expected: list[float], places: int = 9) -> None:
        self.assertEqual(len(actual), len(expected))
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e, places=places)

    def test_d003_projection(self):
        self.assertEqual(matmul([[1, 2, 3, 4]], [[1, 0], [0, 1], [1, 1], [-1, 0]]), [[0, 5]])

    def test_d003_collision(self):
        self.assertEqual(matmul([[1, 0], [0, 1]], [[1], [1]]), [[1], [1]])

    def test_d004_distribution(self):
        self.close(softmax([0, math.log(2), math.log(3)]), [1/6, 2/6, 3/6])

    def test_d004_shift_invariance(self):
        self.close(softmax([0, math.log(2)]), [1/3, 2/3])
        self.close(softmax([10, math.log(2)+10]), [1/3, 2/3])

    def test_d005_transpose_not_reshape(self):
        x = [[1, 2, 3], [4, 5, 6]]
        transpose = [list(col) for col in zip(*x)]
        flat = [v for row in x for v in row]
        reshaped = [flat[i:i+2] for i in range(0, 6, 2)]
        self.assertEqual(transpose, [[1, 4], [2, 5], [3, 6]])
        self.assertEqual(reshaped, [[1, 2], [3, 4], [5, 6]])
        self.assertNotEqual(transpose, reshaped)

    def test_d010_weighted_values(self):
        self.close(matmul([[.2, .3, .5]], [[2, 0], [0, 4], [2, 2]])[0], [1.4, 2.2])

    def test_d012_small_pe(self):
        d = 4
        frequencies = [10000**(-2*i/d) for i in range(d//2)]
        self.close(frequencies, [1, .01])
        self.close([v for w in frequencies for v in (math.sin(0*w), math.cos(0*w))], [0, 1, 0, 1])
        self.assertEqual(512//2, 256)

    def test_d013_head_widths(self):
        self.assertEqual(512//8, 64)
        self.assertEqual(12//3, 4)
        self.assertEqual(3*4, 12)

    def test_d015_loss(self):
        self.assertEqual(.5*(1*2+0-5)**2, 4.5)
        self.assertEqual(.5*(2*2+1-5)**2, 0)

    def test_d016_derivative(self):
        f = lambda w: (w-3)**2
        eps = 1e-5
        for w, expected in [(1, -4), (3, 0), (5, 4)]:
            self.assertAlmostEqual((f(w+eps)-f(w-eps))/(2*eps), expected, places=7)

    def test_d017_step_sizes(self):
        self.assertEqual(1-.25*(-4), 2)
        self.assertEqual((2-3)**2, 1)
        self.assertEqual(1-2*(-4), 9)
        self.assertEqual((9-3)**2, 36)
        self.close([2-.1*3, -1-.1*(-4)], [1.7, -.6])

    def test_d018_chain_gradients(self):
        f = lambda a, b: .5*(b*a*2-8)**2
        eps = 1e-5
        da = (f(1+eps, 3)-f(1-eps, 3))/(2*eps)
        db = (f(1, 3+eps)-f(1, 3-eps))/(2*eps)
        self.close([da, db], [-12, -4], places=7)
        self.close([1-.01*da, 3-.01*db], [1.12, 3.04], places=7)

    def test_d020_matrix_gradients(self):
        self.assertEqual(matmul([[1], [2]], [[3, 4]]), [[3, 4], [6, 8]])
        self.assertEqual(matmul([[3, 4]], [[1, 0], [0, 1]]), [[3, 4]])

    def test_d021_step_counts(self):
        self.assertEqual((120//12, 120//24, 40//4), (10, 5, 10))

    def test_d022_momentum(self):
        self.assertAlmostEqual(.9*2-1, .8)

    def test_d023_cross_entropy(self):
        self.close([-math.log(p) for p in [.5, .25, .1, .2]], [.69314718056, 1.38629436112, 2.30258509299, 1.60943791243])

    def test_d026_joint_update(self):
        residual = 2*3*1-5
        self.assertEqual(.5*residual**2, .5)
        self.close([2-.1*residual*3, 3-.1*residual*2], [1.7, 2.8])

    def test_d028_residual(self):
        self.close([1+.5, -2+.5], [1.5, -1.5])

    def test_d029_normalizations(self):
        x = [1, 3]
        mean = sum(x)/2
        variance = sum((v-mean)**2 for v in x)/2
        self.close([(v-mean)/math.sqrt(variance) for v in x], [-1, 1])
        self.close([v/math.sqrt(sum(t*t for t in x)/2) for v in x], [1/math.sqrt(5), 3/math.sqrt(5)])

    def test_d030_cross_attention_shapes(self):
        q = [[1, 0, 0], [0, 1, 0]]
        kt = [[1]*5, [2]*5, [3]*5]
        scores = matmul(q, kt)
        output = matmul([softmax(row) for row in scores], [[1, 2, 3, 4] for _ in range(5)])
        self.assertEqual((len(scores), len(scores[0])), (2, 5))
        self.assertEqual((len(output), len(output[0])), (2, 4))

    def test_d031_logits(self):
        self.assertEqual(matmul([[1, 2]], [[1, 0, -1], [0, 1, 1]]), [[1, 2, 1]])

    def test_d038_renormalization(self):
        self.close([.5/.8, .3/.8], [.625, .375])

    def test_d039_cache_count(self):
        self.assertEqual(2*1*2*5*4, 80)
        self.assertEqual(2*1*2*6*4, 96)

    def test_d040_rotation_identity(self):
        rotate = lambda v, t: [math.cos(t)*v[0]-math.sin(t)*v[1], math.sin(t)*v[0]+math.cos(t)*v[1]]
        q, k, m, n, theta = [1., 2.], [3., -1.], 3, 10, .1
        rq, rk = rotate(q, m*theta), rotate(k, n*theta)
        lhs = sum(a*b for a, b in zip(rq, rk))
        rhs = sum(a*b for a, b in zip(q, rotate(k, (n-m)*theta)))
        self.assertAlmostEqual(lhs, rhs, places=10)

    def test_d042_parameter_count(self):
        self.assertEqual(8*6, 48)
        self.assertEqual(8*2+2*6, 28)

    def test_d048_similarities(self):
        q, a, b = [1., 0.], [2., 0.], [1., 1.]
        dot = lambda x, y: sum(v*w for v, w in zip(x, y))
        norm = lambda x: math.sqrt(dot(x, x))
        self.close([dot(q, a), dot(q, b)], [2, 1])
        self.close([dot(q, a)/(norm(q)*norm(a)), dot(q, b)/(norm(q)*norm(b))], [1, 1/math.sqrt(2)])


if __name__ == '__main__':
    unittest.main(verbosity=2)
