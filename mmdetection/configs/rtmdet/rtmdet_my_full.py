_base_ = './my_rtmdet_l_8xb32-300e_coco.py'

load_from = './checkpoint/rtmdet_l_8xb32-300e_coco_20220719_112030-5a0be7c4.pth'

model = dict(
    bbox_head=dict(
        num_classes=2))

data_root = '<YOUR ROOT>/'
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
        ann_file='<YOUR DATASET>/train_non_text.json',
        data_prefix=dict(img='<YOUR DATASET>/images/')))
val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='<YOUR DATASET>/test_non_text.json',
        data_prefix=dict(img='<YOUR DATASET>/images/')))
test_dataloader = val_dataloader

# Modify metric related settings
val_evaluator = dict(ann_file=data_root + '<YOUR DATASET>/test_non_text.json')
test_evaluator = val_evaluator

interval = 1
max_epochs = 10

train_cfg = dict(
    max_epochs=max_epochs,
    val_begin=0,
    val_interval=interval)
default_hooks = dict(
    checkpoint=dict(
        interval=interval,
        max_keep_ckpts=20
    ))