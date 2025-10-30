from recbole.quick_start.quick_start import run_recbole

parameter_dict = {
   'learning_rate': 0.001,    #0.001
   'train_batch_size': 2048, 
   'eval_batch_size': 2048,
   'train_neg_sample_args': None,   #
   'neg_sampling': None,
   'mask_ratio': 0.2,
   'hidden_size': 128,
   'inner_size': 128,
   'n_layers': 1,
   'n_heads': 8,
   'hidden_dropout_prob': 0.2,
   'attn_dropout_prob': 0.2,
   'hidden_act': 'gelu',
   'layer_norm_eps': 1e-12,
   'initializer_range': 0.02,
   'eval_args': {'split': {'LS': 'valid_and_test'}, 'order': 'TO', 'mode': 'pop100', 'group_by': 'user'},
   'topk': 10,
   'metrics': ['Recall', 'MRR', 'NDCG'],
   'valid_metric': 'NDCG@10'
}
run_recbole(model='GLINT-RU', dataset='ml-1m', config_dict=parameter_dict)




