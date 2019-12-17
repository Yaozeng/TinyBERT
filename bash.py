import os

os.system("python task_distill.py --pred_distill --aug_train --teacher_model=pretrained/checkpoint-31280/ --student_model=output --output_dir=output2 --train_batch_size=384 --eval_batch_size=128 --learning_rate=3e-5 --num_train_epochs=3.0")