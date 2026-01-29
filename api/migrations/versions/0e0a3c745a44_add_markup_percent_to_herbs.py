"""add markup_percent to herbs

Revision ID: 0e0a3c745a44
Revises: f2bb4fd760b4
Create Date: 2026-01-28
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0e0a3c745a44"
down_revision = "f2bb4fd760b4"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "herbs",
        sa.Column(
            "markup_percent",
            sa.Numeric(5, 2),
            nullable=False,
            server_default="0",
        ),
    )


def downgrade():
    op.drop_column("herbs", "markup_percent")