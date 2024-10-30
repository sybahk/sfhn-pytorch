from datetime import datetime


import submitit

job_name = "SFHN"
bash_files = ["debug_SFHN.sh"]


def get_func(bash_file):
    return submitit.helpers.CommandFunction(
        [
            "bash",
            bash_file,
        ]
    )


now = datetime.now()
time = now.strftime("%Y-%m-%d_%H-%M-%S")
executor = submitit.AutoExecutor(folder=f"log_slurm/{job_name}/{time}")
executor.update_parameters(
    slurm_job_name=job_name,
    slurm_nodes=1,
    slurm_time="4-0",
    slurm_partition="batch_grad",
    slurm_gpus_per_task=4,
    slurm_cpus_per_gpu=8,
    slurm_mem_per_gpu="30G",
    slurm_additional_parameters={
        "exclude": "ariel-g[1,3-5],ariel-m1,ariel-k[1-2],ariel-v[1-13]"
    },
)
print(f"executing {job_name}")
jobs = []
for bash_file in bash_files:
    func = get_func(bash_file)
    job = executor.submit(func)
    jobs.append(job)

job_name = "RCAN"
bash_files = ["debug_RCAN.sh"]

now = datetime.now()
time = now.strftime("%Y-%m-%d_%H-%M-%S")
executor = submitit.AutoExecutor(folder=f"log_slurm/{job_name}/{time}")
executor.update_parameters(
    slurm_job_name=job_name,
    slurm_nodes=1,
    slurm_time="4-0",
    slurm_partition="batch_grad",
    slurm_gpus_per_task=4,
    slurm_cpus_per_gpu=8,
    slurm_mem_per_gpu="30G",
    slurm_additional_parameters={
        "exclude": "ariel-g[1,3-5],ariel-m1,ariel-k[1-2],ariel-v[1-13]"
    },
)
print(f"executing {job_name}")
jobs = []
for bash_file in bash_files:
    func = get_func(bash_file)
    job = executor.submit(func)
    jobs.append(job)
