"""User table

Revision ID: a645a50b0a8d
Revises: db6ae48bb9d4
Create Date: 2024-07-30 06:35:23.669905

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a645a50b0a8d'
down_revision: Union[str, None] = 'db6ae48bb9d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',
                    sa.Column('id',sa.Integer,nullable=False),
                    sa.Column('email',sa.String,nullable=False),
                    sa.Column('password',sa.String,nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,
                              server_default=sa.text('now()')),
                    sa.UniqueConstraint('email'),
                    sa.PrimaryKeyConstraint('id')
                    )
    pass


def downgrade() -> None:
    pass
