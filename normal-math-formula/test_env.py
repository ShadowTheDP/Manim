import requests
import numpy as np
import sys

def test_environment():
    print(f"Python 版本: {sys.version}")
    print(f"虛擬環境路徑: {sys.prefix}")
    
    try:
        # 測試 requests
        response = requests.get("https://www.google.com")
        print(f"Requests 測試成功! 狀態碼: {response.status_code}")
        
        # 測試 numpy
        arr = np.array([1, 2, 3, 4, 5])
        print(f"Numpy 測試成功! 陣列平均值: {arr.mean()}")
        
        print("\n[成功] 虛擬環境與套件運作正常！")
    except ImportError as e:
        print(f"\n[錯誤] 找不到套件: {e}")
        print("請確保已啟動虛擬環境並安裝了 requests 與 numpy。")
    except Exception as e:
        print(f"\n[發生錯誤]: {e}")

if __name__ == "__main__":
    test_environment()
