# KnowComp-Submission-for-WMT23-WLAC-Task

This is the official repository for workshop paper in WMT-WLAC23: [KnowComp Submission for WMT23 Word-Level AutoCompletion Task](http://www2.statmt.org/wmt23/pdf/2023.wmt-1.79.pdf). 

![Overview](./overview.png)


### **Cite this work**
Please use the bibtex below to cite the paper:
```bibtex
@InProceedings{wu-EtAl:2023:WMT6,
  author    = {Wu, Yi  and  Shi, Haochen  and  Wang, Weiqi  and  Song, Yangqiu},
  title     = {KnowComp Submission for WMT23 Word-Level AutoCompletion Task},
  booktitle      = {Proceedings of the Eighth Conference on Machine Translation},
  month          = {December},
  year           = {2023},
  address        = {Singapore},
  publisher      = {Association for Computational Linguistics},
  pages     = {880--887},
  abstract  = {The NLP community has recently witnessed the success of Large Language Models (LLMs) across various Natural Language Processing (NLP) tasks. However, the potential of LLMs for word-level auto-completion in a multilingual context has not been thoroughly explored yet. To address this gap and benchmark the performance of LLMs, we propose an LLM-based system for the WMT23 Word-Level Auto-Completion (WLAC) task. Our system utilizes ChatGPT to represent LLMs and evaluates its performance in three translation directions: Chinese-English, German-English, and English-German. We also study the task under zero-shot and few-shot settings to assess the potential benefits of incorporating exemplars from the training set in guiding the LLM to perform the task. The results of our experiments show that, on average, our system attains a 29.8\% accuracy on the test set. Further analyses reveal that LLMs struggle with WLAC in the zero-shot setting, but performance significantly improves with the help of additional exemplars, though some common errors still appear frequently. These findings have important implications for incorporating LLMs into computer-aided translation systems, as they can potentially enhance the quality of translations. Our codes for evaluation are available at https://github.com/ethanyiwu/WLAC.},
  url       = {https://aclanthology.org/2023.wmt-1.79}
}
```
