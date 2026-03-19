import streamlit as st
import json
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# -------- Load & Execute Notebook --------
@st.cache_resource
def load_notebook():
    with open("orchestrator.ipynb") as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=120, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": "./"}})

    # Extract functions from notebook
    global_vars = {}
    for cell in nb.cells:
        if cell.cell_type == "code":
            exec(cell.source, global_vars)

    return global_vars


# -------- Load functions --------
nb_funcs = load_notebook()

generate_response = nb_funcs.get("generate_response")
run_all_evaluations = nb_funcs.get("run_all_evaluations")


# -------- UI --------
st.set_page_config(page_title="LLM Orchestrator", layout="wide")

st.title("🚀 Intent-Based LLM Orchestrator")

prompt = st.text_area("Enter Prompt", height=150)

if st.button("Run"):

    if not prompt.strip():
        st.warning("Enter a prompt first")
    else:
        with st.spinner("Running..."):

            try:
                response = generate_response(prompt)

                st.subheader("Response")
                st.write(response)

                result = run_all_evaluations(prompt, response)

                st.subheader("Evaluation Summary")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Average Score", result.get("average_score"))

                final = result.get("final_evaluation", {})

                with col2:
                    st.metric("Final Score", final.get("final_score"))

                st.markdown("### Summary")
                st.write(final.get("summary"))

                st.markdown("### Issues")

                issues = []
                for name, res in result.get("individual_evaluations", {}).items():
                    if isinstance(res, dict):
                        issues.extend(res.get("issues_detected", []))

                if issues:
                    for i in set(issues):
                        st.write(f"- {i}")
                else:
                    st.write("No major issues")

            except Exception as e:
                st.error(f"Error: {str(e)}")
