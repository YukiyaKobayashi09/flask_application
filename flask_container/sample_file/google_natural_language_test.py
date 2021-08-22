from google.cloud import language_v1
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./sample_file/focal-balm-321409-2c27b8a5090d.json"

# 判定したい文章
text_content = '今日はいい天気だなぁ。'

# 文章のタイプ(↓の２種類から選択)
# PLAIN_TEXT : 普通のテキスト
# HTML       : HTML形式のテキスト
type_ = language_v1.Document.Type.PLAIN_TEXT

# 文章の言語(日本語なら ja , 英語なら en )
language = "ja"
document = {"content": text_content, "type_": type_, "language": language}

# パラメータの文字コード指定(ここはおまじないで UTF8 を指定でOK)
encoding_type = language_v1.EncodingType.UTF8

client = language_v1.LanguageServiceClient()

# client.の後ろの文字でAPIの機能を分けている
# client.analyze_entities         :エンティティ分析
# client.analyze_entity_sentiment :感情エンティティ分析
# client.analyze_syntax           :構文解析
# client.analyze_sentiment        :感情分析
response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})

print(response)