_base_ = './my_co_dino_5scale_swin_l_16xb1_16e_o365tococo2.py'

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

train_cfg = dict(
    val_interval=interval,
    max_epochs=10)
default_hooks = dict(
    checkpoint=dict(
        interval=interval,
        max_keep_ckpts=10
    ))

param_scheduler = [
    dict(
        type='MultiStepLR',
        begin=0,
        end=10,
        by_epoch=True,
        milestones=[8],
        gamma=0.1)
]
