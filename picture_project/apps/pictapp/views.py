
""" 識別名をpictappにしてBlueprintオブジェクトを生成

    ・テンプレートフォルダーは同じディレクトリの'templates_pict'
    ・staticフォルダーは同じディレクトリの'static_pict'
"""
from flask import Blueprint

pictapp = Blueprint(
    'pictapp',
    __name__,
    template_folder='templates_pict',
    static_folder='static_pict',
    )

"""pictappのトップページのルーティングとビューの定義
"""
from flask import render_template
from flask_login import login_required # login_required

# ログイン必須にする
@pictapp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    # top.htmlをレンダリングする
    return render_template('top.html')

"""ログアウトのルーティングとビューの定義
"""
from flask_login import logout_user
from flask import render_template, url_for, redirect

@pictapp.route('/logout')
@login_required
def logout():
    # flask_loginのlogout_user()関数でログイン中のユーザーを
    # ログアウトさせる
    logout_user()
    # ログイン画面のindexビューにリダイレクト
    return redirect(url_for('authapp.index'))


