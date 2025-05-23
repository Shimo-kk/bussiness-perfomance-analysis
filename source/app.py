import streamlit as st

def main():
    # ページ設定
    st.set_page_config(
        page_title="ビジネスパフォーマンス分析",
        page_icon="📊",
        layout="wide"
    )

    # サイドバーの作成
    with st.sidebar:
        st.header("分析設定")
        
        # 期間選択
        period = st.selectbox(
            "分析期間",
            ["過去1ヶ月", "過去3ヶ月", "過去6ヶ月", "過去1年", "全期間"]
        )
        
        # 指標選択
        metric = st.selectbox(
            "分析指標",
            ["売上", "利益", "顧客数", "注文数", "平均注文単価"]
        )
        
        # 部門選択
        department = st.selectbox(
            "部門",
            ["全部門", "営業部", "マーケティング部", "開発部", "管理部"]
        )

    # メインコンテンツ
    st.title("ビジネスパフォーマンス分析ダッシュボード")

    # 選択された設定の表示
    st.write(f"選択された設定:")
    st.write(f"- 期間: {period}")
    st.write(f"- 指標: {metric}")
    st.write(f"- 部門: {department}")

if __name__ == "__main__":
    main()