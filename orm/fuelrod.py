from sqlalchemy import (
    Column,
    DECIMAL,
    Date,
    DateTime,
    ForeignKeyConstraint,
    Index,
    String,
    Table,
    Text,
    text,
)
from sqlalchemy.dialects.mysql import BIGINT, BIT, INTEGER
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
metadata = Base.metadata


class ArchiveCampaignOutbox(Base):
    __tablename__ = "archive_campaign_outbox"

    id = Column(BIGINT(20), primary_key=True)
    user_id = Column(BIGINT(20), index=True)
    campaign_id = Column(BIGINT(20))
    message_hash = Column(String(150, "utf8mb4_unicode_ci"), index=True)
    date_time = Column(String(100, "utf8mb4_unicode_ci"))
    message_id = Column(String(255, "utf8mb4_unicode_ci"), index=True)
    archive_message = Column(BIT(1))
    sender_id = Column(String(15, "utf8mb4_unicode_ci"))
    currency = Column(String(4, "utf8mb4_unicode_ci"), index=True)
    currency_rate = Column(DECIMAL(10, 2), server_default=text("0.00"))
    phone_number = Column(String(150, "utf8mb4_unicode_ci"))
    sms_text = Column(Text(collation="utf8mb4_unicode_ci"))
    network_code = Column(BIGINT(20), index=True, server_default=text("0"))
    character_count = Column(INTEGER(11))
    sms_count = Column(INTEGER(11))
    retry_count = Column(INTEGER(11), server_default=text("0"))
    single_sms_cost = Column(DECIMAL(10, 2))
    message_string_cost = Column(String(25, "utf8mb4_unicode_ci"))
    message_cost = Column(DECIMAL(10, 2))
    actual_cost = Column(DECIMAL(10, 2), index=True)
    delivery_status = Column(String(100, "utf8mb4_unicode_ci"), index=True)
    message_delivered = Column(BIT(1))
    failure_reason = Column(String(100, "utf8mb4_unicode_ci"))
    created_at = Column(
        DateTime, index=True, server_default=text("current_timestamp()")
    )
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))


class ArchiveSmsOutbox(Base):
    __tablename__ = "archive_sms_outbox"

    id = Column(BIGINT(20), primary_key=True)
    user_id = Column(BIGINT(20), index=True)
    campaign_id = Column(BIGINT(20))
    message_hash = Column(String(150, "utf8mb4_unicode_ci"), index=True)
    date_time = Column(String(100, "utf8mb4_unicode_ci"))
    message_id = Column(String(255, "utf8mb4_unicode_ci"), index=True)
    archive_message = Column(BIT(1))
    sender_id = Column(String(15, "utf8mb4_unicode_ci"))
    currency = Column(String(4, "utf8mb4_unicode_ci"), index=True)
    currency_rate = Column(DECIMAL(10, 2), server_default=text("0.00"))
    phone_number = Column(String(150, "utf8mb4_unicode_ci"))
    sms_text = Column(Text(collation="utf8mb4_unicode_ci"))
    network_code = Column(BIGINT(20), index=True, server_default=text("0"))
    character_count = Column(INTEGER(11))
    sms_count = Column(INTEGER(11))
    retry_count = Column(INTEGER(11), server_default=text("0"))
    single_sms_cost = Column(DECIMAL(10, 2))
    message_string_cost = Column(String(25, "utf8mb4_unicode_ci"))
    message_cost = Column(DECIMAL(10, 2))
    actual_cost = Column(DECIMAL(10, 2), index=True)
    delivery_status = Column(String(100, "utf8mb4_unicode_ci"), index=True)
    message_delivered = Column(BIT(1))
    failure_reason = Column(String(100, "utf8mb4_unicode_ci"))
    created_at = Column(
        DateTime, index=True, server_default=text("current_timestamp()")
    )
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))


class CampaignOutbox(Base):
    __tablename__ = "campaign_outbox"

    id = Column(BIGINT(20), primary_key=True)
    user_id = Column(BIGINT(20), index=True)
    campaign_id = Column(BIGINT(20))
    message_hash = Column(String(150, "utf8mb4_unicode_ci"), index=True)
    date_time = Column(String(100, "utf8mb4_unicode_ci"))
    message_id = Column(String(255, "utf8mb4_unicode_ci"), index=True)
    archive_message = Column(BIT(1))
    sender_id = Column(String(15, "utf8mb4_unicode_ci"))
    currency = Column(String(4, "utf8mb4_unicode_ci"), index=True)
    currency_rate = Column(DECIMAL(10, 2), server_default=text("0.00"))
    phone_number = Column(String(150, "utf8mb4_unicode_ci"))
    sms_text = Column(Text(collation="utf8mb4_unicode_ci"))
    network_code = Column(BIGINT(20), index=True, server_default=text("0"))
    character_count = Column(INTEGER(11))
    sms_count = Column(INTEGER(11))
    retry_count = Column(INTEGER(11), server_default=text("0"))
    single_sms_cost = Column(DECIMAL(10, 2))
    message_string_cost = Column(String(25, "utf8mb4_unicode_ci"))
    message_cost = Column(DECIMAL(10, 2))
    actual_cost = Column(DECIMAL(10, 2), index=True)
    delivery_status = Column(String(100, "utf8mb4_unicode_ci"), index=True)
    message_delivered = Column(BIT(1))
    failure_reason = Column(String(100, "utf8mb4_unicode_ci"))
    created_at = Column(
        DateTime, index=True, server_default=text("current_timestamp()")
    )
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))


t_fuelrod_migration = Table(
    "fuelrod_migration",
    metadata,
    Column("ID", String(255, "utf8mb4_unicode_ci"), nullable=False),
    Column("AUTHOR", String(255, "utf8mb4_unicode_ci"), nullable=False),
    Column("FILENAME", String(255, "utf8mb4_unicode_ci"), nullable=False),
    Column("DATEEXECUTED", DateTime, nullable=False),
    Column("ORDEREXECUTED", INTEGER(11), nullable=False),
    Column("EXECTYPE", String(10, "utf8mb4_unicode_ci"), nullable=False),
    Column("MD5SUM", String(35, "utf8mb4_unicode_ci")),
    Column("DESCRIPTION", String(255, "utf8mb4_unicode_ci")),
    Column("COMMENTS", String(255, "utf8mb4_unicode_ci")),
    Column("TAG", String(255, "utf8mb4_unicode_ci")),
    Column("LIQUIBASE", String(20, "utf8mb4_unicode_ci")),
    Column("CONTEXTS", String(255, "utf8mb4_unicode_ci")),
    Column("LABELS", String(255, "utf8mb4_unicode_ci")),
    Column("DEPLOYMENT_ID", String(10, "utf8mb4_unicode_ci")),
)


class FuelrodMigrationLock(Base):
    __tablename__ = "fuelrod_migration_lock"

    ID = Column(INTEGER(11), primary_key=True)
    LOCKED = Column(BIT(1), nullable=False)
    LOCKGRANTED = Column(DateTime)
    LOCKEDBY = Column(String(255))


class IncomingMessage(Base):
    __tablename__ = "incoming_message"

    id = Column(BIGINT(20), primary_key=True)
    message_id = Column(String(200, "utf8mb4_unicode_ci"), nullable=False)
    link_id = Column(String(200, "utf8mb4_unicode_ci"), nullable=False)
    message = Column(Text(collation="utf8mb4_unicode_ci"), nullable=False)
    short_code = Column(String(50, "utf8mb4_unicode_ci"), nullable=False)
    phone_number = Column(String(30, "utf8mb4_unicode_ci"), nullable=False)
    date_sent = Column(String(30, "utf8mb4_unicode_ci"))
    created_at = Column(DateTime, server_default=text("current_timestamp()"))
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))


class MobileNetwork(Base):
    __tablename__ = "mobile_network"

    id = Column(BIGINT(20), primary_key=True)
    country = Column(String(150, "utf8mb4_unicode_ci"))
    country_code = Column(String(5, "utf8mb4_unicode_ci"))
    mcc_code = Column(INTEGER(11))
    mcc_ref = Column(BIGINT(20), unique=True)
    mnc_code = Column(INTEGER(11))
    network_name = Column(String(200, "utf8mb4_unicode_ci"))
    mobile_code = Column(INTEGER(11))
    created_at = Column(DateTime, server_default=text("current_timestamp()"))
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))

    sms_outbox = relationship("SmsOutbox", back_populates="mobile_network")


class NumberBlacklist(Base):
    __tablename__ = "number_blacklist"

    id = Column(BIGINT(20), primary_key=True)
    phone_number = Column(String(150, "utf8mb4_unicode_ci"))
    sender_id = Column(String(15, "utf8mb4_unicode_ci"))
    created_at = Column(DateTime, server_default=text("current_timestamp()"))
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))


class OptOut(Base):
    __tablename__ = "opt_out"

    id = Column(BIGINT(20), primary_key=True)
    sender_id = Column(String(15, "utf8mb4_unicode_ci"))
    phone_number = Column(String(25, "utf8mb4_unicode_ci"))
    created_at = Column(DateTime, server_default=text("current_timestamp()"))
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))


class RemoteConfig(Base):
    __tablename__ = "remote_config"
    __table_args__ = (
        Index("config-name-uk", "app_name", "config_name", unique=True),
        {"comment": "Table to store remote configuration options"},
    )

    id = Column(BIGINT(20), primary_key=True)
    app_name = Column(String(50, "utf8mb4_unicode_ci"), nullable=False)
    config_name = Column(String(50, "utf8mb4_unicode_ci"), nullable=False)
    config_value = Column(Text(collation="utf8mb4_unicode_ci"), nullable=False)
    created_at = Column(DateTime, server_default=text("current_timestamp()"))
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))


class UntrackedCallback(Base):
    __tablename__ = "untracked_callback"
    __table_args__ = {"comment": "Table to track unsaved callbacks"}

    id = Column(BIGINT(20), primary_key=True)
    message_id = Column(
        String(250, "utf8mb4_unicode_ci"), nullable=False, comment="message identifier"
    )
    network_code = Column(String(50, "utf8mb4_unicode_ci"))
    phone_number = Column(String(100, "utf8mb4_unicode_ci"))
    message_status = Column(String(100, "utf8mb4_unicode_ci"))
    retry_count = Column(INTEGER(11))
    failure_reason = Column(String(100, "utf8mb4_unicode_ci"))
    created_at = Column(DateTime, server_default=text("current_timestamp()"))
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))


class Users(Base):
    __tablename__ = "users"

    id = Column(BIGINT(20), primary_key=True)
    uuid = Column(String(64, "utf8mb4_unicode_ci"), nullable=False, unique=True)
    user_role = Column(
        String(8, "utf8mb4_unicode_ci"), nullable=False, server_default=text("'USER'")
    )
    username = Column(String(18, "utf8mb4_unicode_ci"), unique=True)
    client_name = Column(String(200, "utf8mb4_unicode_ci"))
    user_email = Column(String(50, "utf8mb4_unicode_ci"))
    password = Column(String(200, "utf8mb4_unicode_ci"))
    message_cost = Column(DECIMAL(10, 2), server_default=text("1.50"))
    queue_message = Column(BIT(1))
    overdraft = Column(BIT(1))
    enabled = Column(BIT(1))
    account_status = Column(String(50, "utf8mb4_unicode_ci"))
    created_at = Column(DateTime, server_default=text("current_timestamp()"))
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))

    fee_endpoints = relationship("FeeEndpoints", back_populates="users")
    sms_campaign = relationship("SmsCampaign", back_populates="users")
    sms_statistics = relationship("SmsStatistics", back_populates="user")
    user_api_config = relationship("UserApiConfig", back_populates="users")
    user_sms_credit = relationship("UserSmsCredit", back_populates="users")
    user_tokens = relationship("UserTokens", back_populates="users")


class FeeEndpoints(Base):
    __tablename__ = "fee_endpoints"
    __table_args__ = (
        ForeignKeyConstraint(
            ["username"], ["users.username"], name="fk-endpoint-username"
        ),
    )

    id = Column(BIGINT(20), primary_key=True)
    username = Column(String(18, "utf8mb4_unicode_ci"), nullable=False, unique=True)
    data_endpoint = Column(String(120, "utf8mb4_unicode_ci"), nullable=False)
    created_at = Column(DateTime, server_default=text("current_timestamp()"))
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))

    users = relationship("Users", back_populates="fee_endpoints")


class SmsCampaign(Base):
    __tablename__ = "sms_campaign"
    __table_args__ = (
        ForeignKeyConstraint(
            ["user_uuid"],
            ["users.uuid"],
            onupdate="CASCADE",
            name="user-campaign-uid-fk",
        ),
    )

    id = Column(BIGINT(20), primary_key=True)
    user_uuid = Column(String(64, "utf8mb4_unicode_ci"), nullable=False, index=True)
    campaign_name = Column(String(255, "utf8mb4_unicode_ci"), nullable=False)
    campaign_status = Column(String(100, "utf8mb4_unicode_ci"), index=True)
    is_draft = Column(BIT(1))
    created_at = Column(DateTime, server_default=text("current_timestamp()"))
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))

    users = relationship("Users", back_populates="sms_campaign")
    message_queue = relationship("MessageQueue", back_populates="campaign")


class SmsOutbox(Base):
    __tablename__ = "sms_outbox"
    __table_args__ = (
        ForeignKeyConstraint(
            ["network_code"],
            ["mobile_network.mcc_ref"],
            onupdate="CASCADE",
            name="fk_network_code",
        ),
    )

    id = Column(BIGINT(20), primary_key=True)
    user_id = Column(BIGINT(20), index=True)
    campaign_id = Column(BIGINT(20))
    message_hash = Column(String(150, "utf8mb4_unicode_ci"), index=True)
    date_time = Column(String(100, "utf8mb4_unicode_ci"))
    message_id = Column(String(255, "utf8mb4_unicode_ci"), index=True)
    archive_message = Column(BIT(1))
    sender_id = Column(String(15, "utf8mb4_unicode_ci"))
    currency = Column(String(4, "utf8mb4_unicode_ci"), index=True)
    currency_rate = Column(DECIMAL(10, 2), server_default=text("0.00"))
    phone_number = Column(String(150, "utf8mb4_unicode_ci"))
    sms_text = Column(Text(collation="utf8mb4_unicode_ci"))
    network_code = Column(BIGINT(20), index=True, server_default=text("0"))
    character_count = Column(INTEGER(11))
    sms_count = Column(INTEGER(11))
    retry_count = Column(INTEGER(11), server_default=text("0"))
    single_sms_cost = Column(DECIMAL(10, 2))
    message_string_cost = Column(String(25, "utf8mb4_unicode_ci"))
    message_cost = Column(DECIMAL(10, 2))
    actual_cost = Column(DECIMAL(10, 2), index=True)
    delivery_status = Column(String(100, "utf8mb4_unicode_ci"), index=True)
    message_delivered = Column(BIT(1))
    failure_reason = Column(String(100, "utf8mb4_unicode_ci"))
    created_at = Column(
        DateTime, index=True, server_default=text("current_timestamp()")
    )
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))

    mobile_network = relationship("MobileNetwork", back_populates="sms_outbox")


class SmsStatistics(Base):
    __tablename__ = "sms_statistics"
    __table_args__ = (
        ForeignKeyConstraint(["user_id"], ["users.id"], name="fk-sms-stats-user-id"),
        {"comment": "Table to store sms statistics"},
    )

    id = Column(BIGINT(20), primary_key=True)
    user_id = Column(BIGINT(20), nullable=False, index=True)
    is_campaign = Column(BIT(1), nullable=False)
    sender_id = Column(String(11, "utf8mb4_unicode_ci"), nullable=False)
    total_recipients = Column(BIGINT(20), nullable=False, index=True)
    total_cost = Column(DECIMAL(10, 2), nullable=False, index=True)
    total_messages = Column(BIGINT(20), nullable=False, index=True)
    message_date = Column(Date, nullable=False, index=True)
    message_start_date = Column(Date, nullable=False, index=True)
    message_end_date = Column(Date, nullable=False, index=True)

    user = relationship("Users", back_populates="sms_statistics")


class UserApiConfig(Base):
    __tablename__ = "user_api_config"
    __table_args__ = (
        ForeignKeyConstraint(
            ["user_uuid"], ["users.uuid"], onupdate="CASCADE", name="user_uid_fk"
        ),
        Index("unique_user_sender_id", "id", "sender_id", unique=True),
        Index("unique_user_service", "id", "msg_service", unique=True),
    )

    id = Column(BIGINT(20), primary_key=True)
    user_uuid = Column(String(64, "utf8mb4_unicode_ci"), nullable=False, index=True)
    msg_service = Column(String(20, "utf8mb4_unicode_ci"), nullable=False)
    service_type = Column(
        String(10, "utf8mb4_unicode_ci"), server_default=text("'BULK_SMS'")
    )
    sender_id = Column(String(11, "utf8mb4_unicode_ci"))
    active = Column(BIT(1))
    created_at = Column(DateTime, server_default=text("current_timestamp()"))
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))

    users = relationship("Users", back_populates="user_api_config")


class UserSmsCredit(Base):
    __tablename__ = "user_sms_credit"
    __table_args__ = (
        ForeignKeyConstraint(
            ["user_uuid"], ["users.uuid"], onupdate="CASCADE", name="user-credit-uid-fk"
        ),
        {"comment": "Table to track user SMS credit top ups"},
    )

    id = Column(BIGINT(20), primary_key=True)
    user_uuid = Column(String(64, "utf8mb4_unicode_ci"), nullable=False, index=True)
    credit_amount = Column(DECIMAL(10, 2), nullable=False, index=True)
    remarks = Column(
        String(150, "utf8mb4_unicode_ci"),
        nullable=False,
        comment="Comments regarding the top up",
    )
    created_at = Column(DateTime, server_default=text("current_timestamp()"))
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))

    users = relationship("Users", back_populates="user_sms_credit")


class UserTokens(Base):
    __tablename__ = "user_tokens"
    __table_args__ = (
        ForeignKeyConstraint(
            ["user_name"],
            ["users.username"],
            ondelete="CASCADE",
            name="jwt_token_username",
        ),
    )

    id = Column(String(64, "utf8mb4_unicode_ci"), primary_key=True, unique=True)
    ip_address = Column(String(50, "utf8mb4_unicode_ci"))
    user_name = Column(String(18, "utf8mb4_unicode_ci"), index=True)
    token = Column(String(200, "utf8mb4_unicode_ci"), unique=True)
    expiry_date = Column(DateTime)
    created_at = Column(DateTime, server_default=text("current_timestamp()"))
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))

    users = relationship("Users", back_populates="user_tokens")


class MessageQueue(Base):
    __tablename__ = "message_queue"
    __table_args__ = (
        ForeignKeyConstraint(
            ["campaign_id"],
            ["sms_campaign.id"],
            ondelete="CASCADE",
            onupdate="CASCADE",
            name="fk-campaign-id",
        ),
    )

    id = Column(BIGINT(20), primary_key=True)
    campaign_id = Column(BIGINT(20), nullable=False, index=True)
    message = Column(Text(collation="utf8mb4_unicode_ci"), nullable=False)
    message_length = Column(INTEGER(11), nullable=False, server_default=text("160"))
    retry_count = Column(INTEGER(11), server_default=text("0"))
    message_hash = Column(String(150, "utf8mb4_unicode_ci"), index=True)
    message_status = Column(String(100, "utf8mb4_unicode_ci"))
    failure_reason = Column(String(100, "utf8mb4_unicode_ci"))
    phone_number = Column(String(150, "utf8mb4_unicode_ci"), index=True)
    number_valid = Column(BIT(1))
    sms_count = Column(INTEGER(11))
    message_cost = Column(DECIMAL(10, 2))
    message_sent = Column(BIT(1))
    created_at = Column(DateTime, server_default=text("current_timestamp()"))
    updated_at = Column(DateTime, server_default=text("current_timestamp()"))

    campaign = relationship("SmsCampaign", back_populates="message_queue")
