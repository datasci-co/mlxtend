# Sebastian Raschka 2014-2016
# mlxtend Machine Learning Library Extensions
# Author: Sebastian Raschka <sebastianraschka.com>
#
# License: BSD 3 clause

import numpy as np


def shuffle_arrays_unison(arrays, random_seed=None):
    """Shuffle NumPy arrays in unison.

    Parameters
    ----------
    arrays : array-like, shape = [n_arrays]
        A list of NumPy arrays.
    random_seed : int (default: None)
        Sets the random state.

    Returns
    ----------
    shuffled_arrays : A list of NumPy arrays after shuffling.

    Examples
    --------

    >>> import numpy as np
    >>> from mlxtend.preprocessing import shuffle_arrays_unison
    >>> X1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> y1 = np.array([1, 2, 3])
    >>> X2, y2 = shuffle_arrays_unison(arrays=[X1, y1], random_state=3)
    >>> assert(X2.all() == np.array([[4, 5, 6], [1, 2, 3], [7, 8, 9]]).all())
    >>> assert(y2.all() == np.array([2, 1, 3]).all())
    >>>
    """
    if random_seed:
        np.random.seed(random_seed)
    n = len(arrays[0])
    for a in arrays:
        assert(len(a) == n)
    idx = np.random.permutation(n)
    return [a[idx] for a in arrays]
