#  ValueError: Input contains NaN, infinity or a value too large for dtype('float64').
# 原因是在从数据库导入的数据中，格式不正确，2344566789493828193949 是int 类型，在用 pandas 读取进来的时候
# 变成了float，导致上面的 ValueError,目前的一个解决思路是类似下面的办法

df['int'] = str(df['int'])

# 现在尝试使用 `Feature-engine`

