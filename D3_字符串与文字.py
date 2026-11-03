def stats(path):
    stats = {}
    with open(path) as f:
        text = f.read()
        stats['lines'] = 0
        stats['words'] = 0
        stats['chars'] = 0
        lines = text.splitlines()
        stats['lines'] = len(lines)#得出行数
        words = []
        for line in lines:
            words.extend(line.split())
        stats['words'] = len(words)

        stats['chars'] = len(text)
        return stats



#任务 2：squeeze_spaces(in_path, out_path)
def squeeze_spaces(in_path, out_path):
    with open(in_path) as f:
        text = f.read()
        lines = text.splitlines()
        with open(out_path, 'w', encoding="utf-8") as w:
            for line in lines:
                line = ' '.join(line.split())
                w.write(line + '\n')
    return out_path

#CSV 算平均
def grade_csv(in_path, out_path):
    with open(in_path) as f:
        text = f.read()
        lines = text.splitlines()
        with open(out_path, 'w', encoding="utf-8") as w:
            for line in lines:
                if not line.strip() :
                    continue
                line = line.split(',')
                sum = 0

                for s in line[1:]:
                    sum += int(s)
                    v = sum /(len(line)-1)

                w.write(f'姓名：{line[0]},总分：{sum},平均分：{v:.2f}.\n')
    return out_path

##每次调用往文件末尾追加一行「时间 + 消息」，不覆盖之前的内容
def append_log(msg, path="log.txt"):
    from datetime import datetime
    with open(path, "a", encoding="utf-8") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S")  + msg + '\n')


if __name__ == "__main__":
    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write("hello world\n")
        f.write("python is fun\n")
    assert stats("sample.txt") == {"lines": 2, "chars": 26, "words": 5}

    with open("empty.txt", "w", encoding="utf-8") as f:
        pass
    assert stats("empty.txt") == {"lines": 0, "chars": 0, "words": 0}

    with open("s1.txt", "w", encoding="utf-8") as f:
        f.write("a    b   c\n")
        f.write("d  e\n")
    squeeze_spaces("s1.txt", "s2.txt")
    with open("s2.txt", encoding="utf-8") as f:
        assert f.read() == "a b c\nd e\n"

    import os
    if os.path.exists("log.txt"):
        os.remove("log.txt")
    append_log("第一条")
    append_log("第二条")
    with open("log.txt", encoding="utf-8") as f:
        lines = f.readlines()
    assert len(lines) == 2

    print("全部通过")






