---



# results

This model is a fine-tuned version of [google/flan-t5-base](https://huggingface.co/google/flan-t5-base) on question/answer pairs scraped from Quora.
It achieves the following results on the evaluation set:
- Loss: 2.9379


## Intended uses & limitations

Closed book question answering. Prefix the inputs with "answer the question: "

## Training and evaluation data

50,000 question/answer pairs scraped from Quora

## Training procedure

Seq2Seq training described here: https://huggingface.co/docs/evaluate/transformers_integrations

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 8
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 3.158         | 1.0   | 5641  | 2.9785          |
| 3.0283        | 2.0   | 11282 | 2.9379          |


### Framework versions

- Transformers 4.32.0
- Pytorch 2.0.0
- Datasets 2.14.4
- Tokenizers 0.13.3
