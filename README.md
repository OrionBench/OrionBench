![TEASER](./teaser.png)
This repository contains the code for the paper "OrionBench: A Benchmark for Chart and Human-Recognizable Object Detection in Infographics". The related data is available on [Huggingface](https://huggingface.co/datasets/OrionBench/OrionBench).

## Evaluating Object Detection Models
Please follow the instructions in [MMDetection](./mmdetection) to set up the environment first.  

We train and test four object detection models using MMDetection: [Faster-Rcnn](./mmdetection/configs/faster_rcnn/faster-rcnn_my_full.py), [YOLOv3](./mmdetection/configs/yolo/yolov3_my_full.py), [RTMDet](./mmdetection/configs/rtmdet/rtmdet_my_full.py), and [Co-DETR](./mmdetection/projects/CO-DETR/configs/codino/co_dino_my_full.py).

Modify "YOUR ROOT" and "YOUR DATASET" in the corresponding four configurations.

Execute the following command to train the models:
```
cd mmdetection
bash tools/dist_train.sh configs/faster_rcnn/faster-rcnn_my_full.py 8 --cfg-options data.samples_per_gpu=1 optimizer_config.cumulative_iters=8 optimizer_config.type="GradientCumulativeOptimizerHook" --work-dir work_dir/faster-rcnn_my_full
bash tools/dist_train.sh configs/yolo/yolov3_my_full.py 8 --cfg-options data.samples_per_gpu=1 optimizer_config.cumulative_iters=8 optimizer_config.type="GradientCumulativeOptimizerHook" --work-dir work_dir/yolov3_my_full
bash tools/dist_train.sh configs/rtmdet/rtmdet_my_full_new.py 8 --cfg-options data.samples_per_gpu=1 optimizer_config.cumulative_iters=8 optimizer_config.type="GradientCumulativeOptimizerHook" --work-dir work_dir/rtmdet_my_full
bash tools/dist_train.sh projects/CO-DETR/configs/codino/co_dino_my_full.py 8 --cfg-options data.samples_per_gpu=1 optimizer_config.cumulative_iters=8 optimizer_config.type="GradientCumulativeOptimizerHook" --work-dir work_dir/codetr_my_full
```

The following figure shows detection results of evaluated object detection models: (a) zero-shot prompting with DINO-X; (b) 4-shot prompting with T-Rex2; (c) 4-shot fine-tuning with Co-DETR; (d) fine-tuning on OrionBench with Co-DETR. Bounding boxes in colors are the predictions for charts and HROs.

![det_qual](./det_qual.png)

Additionally, the InternImage-based model co-developed with the benchmark is available on [Huggingface](https://huggingface.co/OrionBench/InternImage_L_DINO).

## References

Please cite our paper if you use our model or dataset in your research

```
@misc{zhu2025orionbench,
      title={OrionBench: A Benchmark for Chart and Human-Recognizable Object Detection in Infographics}, 
      author={Jiangning Zhu and Yuxing Zhou and Zheng Wang and Juntao Yao and Yima Gu and Yuhui Yuan and Shixia Liu},
      year={2025},
      eprint={2505.17473},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2505.17473}, 
}
```
