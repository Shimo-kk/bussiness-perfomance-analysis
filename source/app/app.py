import os
from dotenv import load_dotenv
import streamlit as st
import sqlite3
from analyzer import VarianceFactorAnalysisOptions, TrendAnalysisOptions, ItemOptions

# .envファイルの読み込み
load_dotenv()

conn = sqlite3.connect(os.getenv("DATABASE_URL"))


def main():
    varianceFactorAnalysisOptions = VarianceFactorAnalysisOptions(
        target_year="",
        target_period="",
        source_year="",
        source_period="",
    )

    itemOptions = ItemOptions(
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

        # 区切り線を追加
        st.divider()

        if analysis_type == "差異要因分析":
            varianceFactorAnalysisOptions.target_year = st.selectbox(
                "分析対象", ["2024", "2023"]
            )

        else:
            # Mejor and Name
            varianceFactorAnalysisOptions.mejor_name = st.selectbox(
                "Mejor and Name", ["AZ - Asian"]
            )

        # 区切り線を追加
        st.divider()

        # Mejor and Name
        itemOptions.mejor_name = st.selectbox("Mejor and Name", ["AZ - Asian"])

        # Minor Sub Product Category and Desc
        itemOptions.product_category = st.selectbox(
            "Minor Sub Product Category and Desc", ["001 - Dumpling"]
        )

        # Product 2 and Name
        itemOptions.product_name = st.selectbox(
            "Product 2 and Name", ["AZ01 - Gyoza", "AZ02 - Potstickers"]
        )

        # Item Desc
        itemOptions.item = st.selectbox(
            "Item Desc",
            ["AJI-CHKN PS .7oz 10/12ct", "AJI-GYO JPN STY PK CK 8/3.18 LB"],
        )

        # Devision Name
        itemOptions.devision_name = st.selectbox(
            "Devision Name",
            ["AJI-CHKN PS .7oz 10/12ct", "AJI-GYO JPN STY PK CK 8/3.18 LB"],
        )

        # Channel Name
        itemOptions.channel_name = st.selectbox(
            "Channel Name",
            ["AJI-CHKN PS .7oz 10/12ct", "AJI-GYO JPN STY PK CK 8/3.18 LB"],
        )

        # 区切り線を追加
        st.divider()

        # 分析ボタン
        if st.button("分析実行", type="primary", use_container_width=True):
            st.session_state["analysis_triggered"] = True

    # メインコンテンツ
    st.title("業績解析ダッシュボード")


if __name__ == "__main__":
    main()
