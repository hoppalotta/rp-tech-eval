import yaml

with open('docker-compose-template.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)

# print(type(data["services"].keys()))

with open('service-names.txt', 'w') as f:
    services = list(data["services"].keys())
    for service in services:
        f.write(service + '\n')
