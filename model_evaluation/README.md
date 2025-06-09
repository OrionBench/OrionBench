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
