#### Coin

# Readme: https://www.zhihu.com/question/315108379?

import numpy as np
import time

to = time.time()

def coin(tot):
    toc      = tot + 1
    category = [1, 5 , 10, 20, 50, 100]
    dp       = np.zeros(toc)            # 0 from 0 to tot
    dp[0]    = 1
    for i in category:
        for j in np.arange(1,toc):      # 1 to tot
            if j >= i:
                dp[j] = dp[j] + dp[j-i]
    return dp[tot]

print(coin(500))

td = time.time() - to
print("The time interval is %f s." %td)