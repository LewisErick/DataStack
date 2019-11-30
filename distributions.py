import numpy as np

def get_distribution(x, columns):
    """
    x : list or matrix, either as a Python list or np.array(preferrable)
    columns : list of column labels
    
    For each of the columns in the matrix or vector:
        - If the columns contain ints, get the pdf that best fits the DISCRETE (count) variable represented.
        - If the columns contain floats, get the pdf that best fits the CONTINUOUS variable represented.
        - If the columns contain str, get the pdf that best fits the treatment of the strs as binary (0 or 1) as independent events.
    """
    if type(x) != list and type(x) != np.array:
        raise Exception("Excepting array-like type, received", str(type(x)), "instead.")
    if type(x) != np.array:
        x = np.array(x)
    x_shape = x.shape
    if len(x_shape) > 2:
        raise Exception("Expecting 1-D array or 2-D array, but got ", str(len(x_shape)), "-D array instead.")
    if len(columns) != x_shape[1]:
        raise Exception("Number of columns in matrix/vector needs to match number of values in columns argument.")
    
    best_fit_distributions = {}
    for i in range(x_shape[1]):
        x_column = x[:, i]
        dtype = x_column.dtype
        dist = None
        if np.issubtype(dtype, np.integer):
            dist = get_distribution_discrete(x_column)
        elif np.issubdtype(dtype, np.float):
            dist = get_distribution_continuous(x_column)
        elif np.issubdtype(dtype, np.string_):
            dist = get_distribution_continuous(x_column)
        else:
            raise Exception("Non-supported type: ", dtype, "expected float, string or int")
        best_fit_distributions[columns[i]] = dist
    
    return best_fit_distributions

def get_distribution_discrete(x):
    '''
    x : list containing discrete numerical values
    '''
    return "discrete"


def get_distribution_continuous(x):
    '''
    x : list containing continuous numerical values
    '''
    return "continuous"

def get_distribution_categorical(x):
    '''
    x : list containing string values representing the categories
    '''
    return "categorical"
