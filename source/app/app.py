import os
from dotenv import load_dotenv
import streamlit as st
import sqlite3
from analyzer import VarianceFactorAnalysisOptions

# .envファイルの読み込み
load_dotenv()

DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "db", "bussiness_perfomance_analysis.db"
)

conn = sqlite3.connect(DB_PATH)


def main():

    varianceFactorAnalysisOptions = VarianceFactorAnalysisOptions(
        mejor_name="",
        product_category="",
        product_name="",
        item="",
        devision_name="",
        channel_name="",
    )

    # ページ設定
    st.set_page_config(
        page_title="業績解析ダッシュボード", page_icon="📊", layout="wide"
    )

    # サイドバーの作成
    with st.sidebar:
        st.header("分析設定")

        # 分析タイプの選択
        analysis_type = st.radio("", ["差異要因分析", "トレンド分析"])

        if analysis_type == "差異要因分析":
            # Mejor and Name
            varianceFactorAnalysisOptions.mejor_name = st.selectbox(
                "Mejor and Name", ["AZ - Asian"]
            )

            # Minor Sub Product Category and Desc
            varianceFactorAnalysisOptions.product_category = st.selectbox(
                "Minor Sub Product Category and Desc", ["001 - Dumpling"]
            )

            # Product 2 and Name
            varianceFactorAnalysisOptions.product_name = st.selectbox(
                "Product 2 and Name", ["AZ01 - Gyoza", "AZ02 - Potstickers"]
            )

            # Item Desc
            varianceFactorAnalysisOptions.item = st.selectbox(
                "Item Desc",
                ["AJI-CHKN PS .7oz 10/12ct", "AJI-GYO JPN STY PK CK 8/3.18 LB"],
            )

            # Devision Name
            varianceFactorAnalysisOptions.devision_name = st.selectbox(
                "Devision Name",
                ["AJI-CHKN PS .7oz 10/12ct", "AJI-GYO JPN STY PK CK 8/3.18 LB"],
            )

            # Channel Name
            varianceFactorAnalysisOptions.channel_name = st.selectbox(
                "Channel Name",
                ["AJI-CHKN PS .7oz 10/12ct", "AJI-GYO JPN STY PK CK 8/3.18 LB"],
            )

        else:
            #
            department = st.selectbox(
                "部門", ["営業部", "マーケティング部", "開発部", "管理部"]
            )

            # 指標選択
            metric = st.selectbox(
                "分析指標", ["売上", "利益", "顧客数", "注文数", "平均注文単価"]
            )

            # 期間選択（部門別分析の場合は全期間固定）
            period = "全期間"

        # 区切り線を追加
        st.divider()

        # 分析ボタン
        if st.button("分析実行", type="primary", use_container_width=True):
            st.session_state["analysis_triggered"] = True

    # メインコンテンツ
    st.title("業績解析ダッシュボード")


if __name__ == "__main__":
    main()
