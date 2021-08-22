import tweepy

# 認証に必要なキーとトークン
# TODO：認証情報の直書きはまずいので、
#       今後設定ファイルから読み込む または 環境変数として設定するなど考える
# TODO：認証情報はGitへコミットする関係上削除しています 
API_KEY             = '***'
API_SECRET          = '***'
ACCESS_TOKEN        = '***'
ACCESS_TOKEN_SECRET = '***'

# APIの認証
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# 特定のユーザのツイートを取得する。countが取得件数の上限。
results = api.user_timeline(screen_name="kingjim", count=10)
print("/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
for result in results:
    print(result.id)
    print(result.created_at)
    print(result.text)
    print("----------------------------------------------------------------------")
    print()
print("/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")

# キーワード検索。countが取得件数の上限。
results2 = api.search(q=["いろはす"], count=10)

print("/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")
for result in results2:
    username = result.user._json['screen_name']
    user_id = result.id
    print("ユーザーID："+str(user_id))
    user = result.user.name
    print("ユーザー名："+user)
    tweet = result.text
    print("ユーザーのコメント："+tweet)
    print("----------------------------------------------------------------------")
    print()
print("/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/")