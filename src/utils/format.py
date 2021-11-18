from flask_restx import fields

# created_at の値を %Y-%m-%d %H:%M:%S 形式にするために
# TimeFormat クラスを作成して format メソッドをオーバーライド
class TimeFormat(fields.DateTime):
    def format(self, value):
        return value.strftime('%Y-%m-%d %H:%M:%S')