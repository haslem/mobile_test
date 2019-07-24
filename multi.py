
from multiprocess import Process
# import try_s3_launch
# import try_s3_launch1
import s3_functions
import s3_functions_copy_grid


if __name__=='__main__':
     p1 = Process(target = s3_functions.s3)
     p1.start()
     p2 = Process(target = s3_functions_copy_grid.nokia)
     p2.start()

     # p1 = Process(target = try_s3_launch.launch)
     # p1.start()
     # p2 = Process(target = try_s3_launch1.launch)
     # p2.start()

   




   