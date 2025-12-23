import argparse


def main():
    # 创建解析器
    parser = argparse.ArgumentParser(description='通过命令行参数执行加减法操作')

    # 定义命令行参数
    parser.add_argument('num1', type=float, help='第一个数字')
    parser.add_argument('num2', type=float, help='第二个数字')
    parser.add_argument('--operation', choices=['add', 'subtract'], default='add',
                        help='选择操作：加法(add)或减法(subtract) [默认: add]')

    # 解析命令行参数
    args = parser.parse_args()

    # 获取参数
    num1 = args.num1
    num2 = args.num2
    operation = args.operation

    # 执行加法或减法
    if operation == 'add':
        result = num1 + num2
        print(f'{num1} + {num2} = {result}')
    elif operation == 'subtract':
        result = num1 - num2
        print(f'{num1} - {num2} = {result}')


if __name__ == "__main__":
    main()
