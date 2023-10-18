python gen_seq.py
python gen_pretrain_data.py
python gen_pseudo_pair.py

CUDA_VISIBLE_DEVICES=0 python run_pretrain.py --checkpointDir=ckpt_dir
CUDA_VISIBLE_DEVICES=1 python run_pseudo_supervision.py --init_checkpoint=ckpt_dir/model_104000

# output embedding
CUDA_VISIBLE_DEVICES=5 python run_embed.py --init_checkpoint=pseudo_ckpt_dir/model_6000
CUDA_VISIBLE_DEVICES=4 python run_embed.py --init_checkpoint=ckpt_dir/model_104000
