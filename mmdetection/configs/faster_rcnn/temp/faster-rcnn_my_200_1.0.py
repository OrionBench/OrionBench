REPLACE1 = 'yuxing/dataset/NIPS_dataset/annotations/mixed_annotations/merged_size200_prop_realworld_1.0.json'
REPLACE2 = 500
REPLACE3 = 50
_base_ = '../faster-rcnn_r50_fpn_1x_coco.py'

model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=2)))

data_root = '/data/'
metainfo = {
    'classes': ('human_recognizable_object', 'chart'),
    'palette': [
        (220, 20, 60), (20, 60, 220), 
    ]
}
train_dataloader = dict(
    batch_size=1,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        # ann_file='yuxing/dataset/NIPS_dataset/annotations/annotations_train.json',
        # data_prefix=dict(img='yuxing/dataset/NIPS_dataset/images/')))
        # ann_file='yuxing/scene-tree-evaluation/tmp2/annotations_full2.json',
        # data_prefix=dict(img='jiangning/Dataset/gt_annotation/')))
        # ann_file='yuxing/dataset/NIPS_dataset/annotations/instances_30.json',
        # data_prefix=dict(img='yuxing/dataset/NIPS_dataset/images/')))
        ann_file=REPLACE1,
        data_prefix=dict(img='yuxing/dataset/NIPS_dataset/images/')))
val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        # ann_file='yuxing/scene-tree-evaluation/tmp2/annotations_full2.json',
        # data_prefix=dict(img='jiangning/Dataset/gt_annotation/')))
        ann_file='yuxing/dataset/NIPS_dataset/annotations/annotations_test.json',
        data_prefix=dict(img='yuxing/dataset/NIPS_dataset/images/')))
test_dataloader = val_dataloader

# Modify metric related settings
val_evaluator = dict(ann_file=data_root + 'yuxing/dataset/NIPS_dataset/annotations/annotations_test.json')
test_evaluator = val_evaluator

interval = REPLACE3
max_epochs = REPLACE2

train_cfg = dict(
    max_epochs=max_epochs,
    val_begin=0,
    val_interval=interval)
default_hooks = dict(
    checkpoint=dict(
        interval=interval,
        max_keep_ckpts=20,
        save_best='coco/bbox_mAP'
    ))

custom_hooks = [dict(type='FRCNNValLoss')]