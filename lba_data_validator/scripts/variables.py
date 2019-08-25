import click

from sqlalchemy.exc import DBAPIError
from pyramid.paster import get_appsettings
from lba_data_validator.models import get_engine
from lba_data_validator.models import get_session_factory, get_session
from lba_data_validator.models.biosphere_atmosphere \
    import BiosphereAtmosphereVariable


@click.group()
@click.pass_context
def cli(ctx):
    settings = get_appsettings('development.ini')

    engine = get_engine(settings, prefix='sqlalchemy.')
    session_factory = get_session_factory(engine)
    dbsession = get_session(session_factory)

    ctx.obj['dbsession'] = dbsession

    return ctx


@cli.command()
@click.pass_context
def list(ctx):
    variables = ctx.obj['dbsession'].query(BiosphereAtmosphereVariable).all()
    click.echo('\n')
    click.echo('='*90)
    click.echo('||  Name\t\t| Minimum Value\t\t\t| Maximum Value')
    click.echo('='*90)
    for variable in variables:
        click.echo('||  {}\t\t| {}\t\t\t\t| {}'.format(
            variable.name, variable.minimum_value, variable.maximum_value))
    click.echo('='*90)


@cli.command()
@click.option('--max-value')
@click.option('--min-value')
@click.option('--name')
@click.pass_context
def create(ctx, name, min_value, max_value):

    try:
        click.echo('Creating variable {}...'.format(name))
        dbsession = ctx.obj['dbsession']
        variable = BiosphereAtmosphereVariable(name=name,
                                               minimum_value=min_value,
                                               maximum_value=max_value)
        dbsession.add(variable)
        dbsession.flush()

    except DBAPIError as e:

        click.echo('Error: Database error has occured! Raised {}'
                   .format(e.__class__.__name__))

        dbsession.close()

        return

    dbsession.commit()
    dbsession.close()

    click.echo('Variable {} successfully created'.format(name))

    return


if __name__ == '__main__':
    cli(obj={})
