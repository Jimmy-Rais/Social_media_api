"""add column

Revision ID: db6ae48bb9d4
Revises: 8a08e14e1fc1
Create Date: 2024-07-30 06:33:27.679099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db6ae48bb9d4'
down_revision: Union[str, None] = '8a08e14e1fc1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts',
                    sa.Column('id',sa.Integer,primary_key=True,nullable=False),
                    sa.Column('title',sa.String,nullable=False),
                    sa.Column('content',sa.String,nullable=False)
                    )
    pass


def downgrade():
    op.drop_table('posts')
    pass

