import argparse
import shutil
import sys
from pathlib import Path


def main():
    # 引数の定義
    parser = argparse.ArgumentParser(
        description='指定したパスに存在するファイルを拡張子ごとに収集')
    parser.add_argument('--src', default='.', help='収集対象ディレクトリ')
    parser.add_argument('--dst', default='.', help='保存先ディレクトリ')
    args = parser.parse_args()

    # 引数の値を取得
    src = Path(args.src)
    dst = Path(args.dst)

    # 収集対象ディレクトリおよび保存先ディレクトリが存在しなければ終了
    if not src.exists():
        print('エラー: 収集対象ディレクトリ {} が見つかりませんでした'.format(str(src)))
    if not dst.exists():
        print('エラー: 保存先ディレクトリ {} が見つかりませんでした'.format(str(dst)))
    if not src.exists() or not dst.exists():
        sys.exit(1)

    # 収集処理
    for p in src.iterdir():
        if p.is_file():
            # 保存先ディレクトリ直下に拡張子の名前でディレクトリを生成
            _dst = dst / (p.suffix[1:])
            _dst.mkdir(exist_ok=True)
            # 生成したディレクトリにファイルを移動
            try:
                shutil.move(p, _dst)
            except shutil.Error:
                print('警告: {} は既に存在します'.format(str(_dst / p.name)))


if __name__ == "__main__":
    main()
