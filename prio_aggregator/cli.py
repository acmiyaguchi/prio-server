import click


def common_arguments(func):
    @click.argument("--bucket", required=True, help="")
    @click.argument("--prefix", required=True, help="")
    @click.argument("--server-id", required=True, help="")
    @click.argument("--public-key-A", required=True, help="")
    @click.argument("--public-key-B", required=True, help="")
    @click.argument("--private-key", required=True, help="")
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def input_owned_argument(func):
    @click.argument("--input-owned", required=True, help="")
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def input_shared_argument(func):
    @click.argument("--input-shared", required=True, help="")
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def output_owned_argument(func):
    @click.argument("--output-owned", required=True, help="")
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def output_shared_argument(func):
    @click.argument("--output-shared", required=True, help="")
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@click.command()
@common_arguments
@input_owned_argument
@output_shared_argument
@output_owned_argument
def create_verify1():
    """Decode a batch of shares"""
    click.echo("Running create_verify1")


@click.command()
@common_arguments
@input_owned_argument
@output_shared_argument
@output_owned_argument
def create_verify2():
    """Verify a batch of SNIPs"""
    click.echo("Running create_verify2")


@click.command()
@common_arguments
@input_owned_argument
@output_shared_argument
@output_owned_argument
def aggregate():
    """Generate an aggregate share from a batch of verified SNIPs"""
    click.echo("Running aggregate")


@click.command()
@common_arguments
@input_owned_argument
@output_shared_argument
@output_owned_argument
def publish():
    """Generate a final aggregate and remap data to a content blocklist"""
    click.echo("Running publish")
