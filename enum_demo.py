# 枚举（Enum）是一种独特的数据类型，由一组元素或成员值组成。
# 这些成员是代表特定数值的常量，这使得变量值需要限定在预定义集合内时非常有用。

"""
枚举的使用场景:
(1)状态管理：跟踪对象的状态，例如流程的阶段（例如待处理、处理中、已完成）。
(2)配置选项：设置仅限于特定选项集的配置值（例如低、中、高）。
(3)分类：对数据进行分类，例如用户类型（例如管理员、用户、访客）。
"""

"""
虽然列表和字典也可以保存相关值，但枚举提供了几个优势：
(1)可读性：与列表或字典相比，枚举以更清晰和更易读的方式定义相关常量。
(2)安全性：枚举防止分配无效值，减少错误的风险。
(3)维护性：枚举更容易维护和更新，特别是在处理大量相关常量时。
"""

from enum import Enum


# 为一周的日期定义一个枚举
class Day(Enum):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7


# 访问枚举成员
print(Day.MONDAY)  # 输出: Day.MONDAY
print(Day.MONDAY.name)  # 输出: MONDAY
print(Day.MONDAY.value)  # 输出: 2


# 在条件中使用枚举
# 检查传入的日期是否为星期六或星期日的函数
def is_weekend(day):
    return day in (Day.SATURDAY, Day.SUNDAY)


print(is_weekend(Day.SATURDAY))  # 输出: True
print(is_weekend(Day.WEDNESDAY))  # 输出: False