from pyvitaisimulator import HECUBE
from pyvitaisimulator import HECUBOID
from pyvitaisimulator import HECYLINDER
from pyvitaisimulator import HEINSERT
from pyvitaisimulator import RMCUBE
from pyvitaisimulator import RMCUBOID
from pyvitaisimulator import RMCYLINDER
from pyvitaisimulator import RMINSERT
import time
import cv2
import numpy as np

def main():
    simulator = RMINSERT()
    simulator.run()
    try:
        while 1:
            start_time = time.time()
            try:
                # 获取最新数据
                depth_img, tact_img, marker_img, origin_marker, current_marker = simulator.get_data()
                tact_resized = cv2.resize(tact_img, (240, 240))  # 宽 240, 高 240
                marker_resized = cv2.resize(marker_img, (240, 240))
                depth_resized = cv2.resize(depth_img, (240, 240))
                combined_img = np.hstack(( tact_resized, marker_resized))
                cv2.imshow("combined_img", combined_img)
                cv2.imshow("depth_resized", depth_resized)
                print('origin_marker.shape ', origin_marker.shape)
                print('current_marker.shape ', current_marker.shape)
                displacement = (current_marker - origin_marker).sum()
                print('displacement ', displacement)
                # 处理用户输入
                key = cv2.waitKey(1) & 0xFF
                if key == 27: # esc
                    break
            except:
                pass

            # 显示刷新率控制
            elapsed = time.time() - start_time
            if elapsed < 0.033:  # 30Hz显示
                time.sleep(0.033 - elapsed)
    finally:
        simulator.cleanup()

if __name__ == '__main__':
    main()