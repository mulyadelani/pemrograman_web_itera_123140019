"""create matakuliah table

Revision ID: 202611240002
Revises: 202611240001
"""
from alembic import op
import sqlalchemy as sa

revision = "202611240002"
down_revision = "202611240001"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "matakuliah",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("kode_mk", sa.Text(), nullable=False),
        sa.Column("nama_mk", sa.Text(), nullable=False),
        sa.Column("sks", sa.Integer(), nullable=False),
        sa.Column("semester", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("kode_mk"),
        sa.CheckConstraint("sks > 0", name="ck_matakuliah_sks_positive"),
        sa.CheckConstraint("semester > 0", name="ck_matakuliah_semester_positive"),
    )


def downgrade():
    op.drop_table("matakuliah")
