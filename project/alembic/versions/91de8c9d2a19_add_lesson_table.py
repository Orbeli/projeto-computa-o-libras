"""add lesson table

Revision ID: 91de8c9d2a19
Revises: 3dec532948a3
Create Date: 2022-05-22 21:54:45.086096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91de8c9d2a19'
down_revision = '3dec532948a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lesson',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('duration', sa.String(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lesson_id'), 'lesson', ['id'], unique=False)
    op.add_column('module', sa.Column('lesson_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'module', 'lesson', ['lesson_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'module', type_='foreignkey')
    op.drop_column('module', 'lesson_id')
    op.drop_index(op.f('ix_lesson_id'), table_name='lesson')
    op.drop_table('lesson')
    # ### end Alembic commands ###
