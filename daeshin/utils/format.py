class Format:
    @staticmethod
    def get_code(code):
        format_code = "{0:0>6}".format(code)
        return f"A{format_code}"