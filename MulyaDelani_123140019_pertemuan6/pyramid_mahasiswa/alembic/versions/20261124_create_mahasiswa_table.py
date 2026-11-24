"""create mahasiswa table

Revision ID: 202611240001
Revises:
"""
from alembic import op
import sqlalchemy as sa

revision = "202611240001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "mahasiswa",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("nim", sa.Text(), nullable=False),
        sa.Column("nama", sa.Text(), nullable=False),
        sa.Column("jurusan", sa.Text(), nullable=False),
        sa.Column("tanggal_lahir", sa.Date(), nullable=True),
        sa.Column("alamat", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("nim"),
    )


def downgrade():
    op.drop_table("mahasiswa")
