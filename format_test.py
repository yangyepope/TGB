class Style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'


# 清除ANSI转义码
def remove_ansi_escape_sequences(text):
    return text.encode('ascii', 'ignore').decode('ascii')


# 使用格式字符串设置文本样式

def print_styled_text(text, color, size):
    print(f"{size}{color}{text}{Style.END}")





