# import numpy as np
#
# arr = np.array([1,2,3,4,5,])
#
# print(arr)
# print(type(arr))

# import numpy as np
#
# arr = np.array(42)
#
# print(arr)

# import numpy as np
#
# x = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#
# print(x)

# import numpy as np
#
# x = np.array([[[1,2,3],[4,5,6]],[[7,8,9], [10,11,12]]])
#
# print(x)

import numpy as np

arr = np.array([1,2,3,4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)