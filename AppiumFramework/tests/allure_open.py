import shutil
import subprocess


def get_allure_exec():
    allures_exe = ['allure.cmd', 'allure.bat', 'allure']
    for allure_exe in allures_exe:
        if shutil.which(allure_exe):
            return allure_exe
    raise OSError(f'Expected allure executables {allures_exe} do not exist!')


if __name__ == '__main__':
    subprocess.check_call([get_allure_exec(), 'generate', '-c'])
    subprocess.check_call([get_allure_exec(), 'open'])
