from typing import Any, List, Optional

from sqlalchemy import Column, DECIMAL, Date, DateTime, ForeignKeyConstraint, Index, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import BIGINT, BIT, INTEGER, LONGTEXT, TINYINT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime
import decimal

class Base(DeclarativeBase):
    pass


class ApiAccounts(Base):
    __tablename__ = 'api_accounts'
    __table_args__ = (
        Index('user_name', 'username', unique=True),
        Index('user_uuid_uk', 'uuid', unique=True)
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    uuid: Mapped[str] = mapped_column(String(64))
    account_type: Mapped[str] = mapped_column(String(15), server_default=text("'CLIENT'"))
    role: Mapped[str] = mapped_column(String(8), server_default=text("'USER'"))
    queue_message: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    overdraft: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    enabled: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    username: Mapped[Optional[str]] = mapped_column(String(18))
    name: Mapped[Optional[str]] = mapped_column(String(200))
    email: Mapped[Optional[str]] = mapped_column(String(50))
    password: Mapped[Optional[str]] = mapped_column(String(200))
    message_cost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), server_default=text('1.50'))
    account_status: Mapped[Optional[str]] = mapped_column(String(50))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))

    api_service: Mapped[List['ApiService']] = relationship('ApiService', back_populates='api_accounts')
    api_sms_credit: Mapped[List['ApiSmsCredit']] = relationship('ApiSmsCredit', back_populates='api_accounts')
    fee_endpoints: Mapped[List['FeeEndpoints']] = relationship('FeeEndpoints', back_populates='api_accounts')
    sms_campaign: Mapped[List['SmsCampaign']] = relationship('SmsCampaign', back_populates='api_accounts')
    sms_statistics: Mapped[List['SmsStatistics']] = relationship('SmsStatistics', back_populates='user')
    user_api_account: Mapped[List['UserApiAccount']] = relationship('UserApiAccount', back_populates='account')


class ArchiveCampaignOutbox(Base):
    __tablename__ = 'archive_campaign_outbox'
    __table_args__ = (
        Index('fk_network_code', 'network_code'),
        Index('idx-actual-cost', 'actual_cost'),
        Index('idx-created-at', 'created_at'),
        Index('idx-currency', 'currency'),
        Index('idx-delivery-status', 'delivery_status'),
        Index('idx-message-id', 'message_id'),
        Index('idx-sms-outbox-hash', 'message_hash'),
        Index('idx-sms-outbox-user-id', 'user_id')
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    archive_message: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    message_delivered: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    user_id: Mapped[Optional[int]] = mapped_column(BIGINT(20))
    campaign_id: Mapped[Optional[int]] = mapped_column(BIGINT(20))
    message_hash: Mapped[Optional[str]] = mapped_column(String(150))
    date_time: Mapped[Optional[str]] = mapped_column(String(100))
    message_id: Mapped[Optional[str]] = mapped_column(String(255))
    sender_id: Mapped[Optional[str]] = mapped_column(String(15))
    currency: Mapped[Optional[str]] = mapped_column(String(4))
    currency_rate: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), server_default=text('0.00'))
    phone_number: Mapped[Optional[str]] = mapped_column(String(150))
    sms_text: Mapped[Optional[str]] = mapped_column(Text)
    network_code: Mapped[Optional[int]] = mapped_column(BIGINT(20), server_default=text('0'))
    character_count: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    sms_count: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    retry_count: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))
    single_sms_cost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    message_string_cost: Mapped[Optional[str]] = mapped_column(String(25))
    message_cost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    actual_cost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    delivery_status: Mapped[Optional[str]] = mapped_column(String(100))
    failure_reason: Mapped[Optional[str]] = mapped_column(String(100))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    archival_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))


class ArchiveSmsOutbox(Base):
    __tablename__ = 'archive_sms_outbox'
    __table_args__ = (
        Index('fk_network_code', 'network_code'),
        Index('idx-actual-cost', 'actual_cost'),
        Index('idx-created-at', 'created_at'),
        Index('idx-currency', 'currency'),
        Index('idx-delivery-status', 'delivery_status'),
        Index('idx-message-id', 'message_id'),
        Index('idx-sms-outbox-hash', 'message_hash'),
        Index('idx-sms-outbox-user-id', 'user_id')
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    archive_message: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    message_delivered: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    user_id: Mapped[Optional[int]] = mapped_column(BIGINT(20))
    campaign_id: Mapped[Optional[int]] = mapped_column(BIGINT(20))
    message_hash: Mapped[Optional[str]] = mapped_column(String(150))
    date_time: Mapped[Optional[str]] = mapped_column(String(100))
    message_id: Mapped[Optional[str]] = mapped_column(String(255))
    sender_id: Mapped[Optional[str]] = mapped_column(String(15))
    currency: Mapped[Optional[str]] = mapped_column(String(4))
    currency_rate: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), server_default=text('0.00'))
    phone_number: Mapped[Optional[str]] = mapped_column(String(150))
    sms_text: Mapped[Optional[str]] = mapped_column(Text)
    network_code: Mapped[Optional[int]] = mapped_column(BIGINT(20), server_default=text('0'))
    character_count: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    sms_count: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    retry_count: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))
    single_sms_cost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    message_string_cost: Mapped[Optional[str]] = mapped_column(String(25))
    message_cost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    actual_cost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    delivery_status: Mapped[Optional[str]] = mapped_column(String(100))
    failure_reason: Mapped[Optional[str]] = mapped_column(String(100))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    archival_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))


class CampaignOutbox(Base):
    __tablename__ = 'campaign_outbox'
    __table_args__ = (
        Index('fk_network_code', 'network_code'),
        Index('idx-actual-cost', 'actual_cost'),
        Index('idx-created-at', 'created_at'),
        Index('idx-currency', 'currency'),
        Index('idx-delivery-status', 'delivery_status'),
        Index('idx-message-id', 'message_id'),
        Index('idx-sms-outbox-hash', 'message_hash'),
        Index('idx-sms-outbox-user-id', 'user_id')
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    archive_message: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    message_delivered: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    user_id: Mapped[Optional[int]] = mapped_column(BIGINT(20))
    campaign_id: Mapped[Optional[int]] = mapped_column(BIGINT(20))
    message_hash: Mapped[Optional[str]] = mapped_column(String(150))
    date_time: Mapped[Optional[str]] = mapped_column(String(100))
    message_id: Mapped[Optional[str]] = mapped_column(String(255))
    sender_id: Mapped[Optional[str]] = mapped_column(String(15))
    currency: Mapped[Optional[str]] = mapped_column(String(4))
    currency_rate: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), server_default=text('0.00'))
    phone_number: Mapped[Optional[str]] = mapped_column(String(150))
    sms_text: Mapped[Optional[str]] = mapped_column(Text)
    network_code: Mapped[Optional[int]] = mapped_column(BIGINT(20), server_default=text('0'))
    character_count: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    sms_count: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    retry_count: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))
    single_sms_cost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    message_string_cost: Mapped[Optional[str]] = mapped_column(String(25))
    message_cost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    actual_cost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    delivery_status: Mapped[Optional[str]] = mapped_column(String(100))
    failure_reason: Mapped[Optional[str]] = mapped_column(String(100))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))


class FailedJobs(Base):
    __tablename__ = 'failed_jobs'
    __table_args__ = (
        Index('failed_jobs_uuid_unique', 'uuid', unique=True),
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    uuid: Mapped[str] = mapped_column(String(255))
    connection: Mapped[str] = mapped_column(Text)
    queue: Mapped[str] = mapped_column(Text)
    payload: Mapped[str] = mapped_column(LONGTEXT)
    exception: Mapped[str] = mapped_column(LONGTEXT)
    failed_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('current_timestamp()'))


t_fuelrod_migration = Table(
    'fuelrod_migration', Base.metadata,
    Column('ID', String(255), nullable=False),
    Column('AUTHOR', String(255), nullable=False),
    Column('FILENAME', String(255), nullable=False),
    Column('DATEEXECUTED', DateTime, nullable=False),
    Column('ORDEREXECUTED', INTEGER(11), nullable=False),
    Column('EXECTYPE', String(10), nullable=False),
    Column('MD5SUM', String(35)),
    Column('DESCRIPTION', String(255)),
    Column('COMMENTS', String(255)),
    Column('TAG', String(255)),
    Column('LIQUIBASE', String(20)),
    Column('CONTEXTS', String(255)),
    Column('LABELS', String(255)),
    Column('DEPLOYMENT_ID', String(10))
)


class FuelrodMigrationLock(Base):
    __tablename__ = 'fuelrod_migration_lock'

    ID: Mapped[int] = mapped_column(INTEGER(11), primary_key=True)
    LOCKED: Mapped[Any] = mapped_column(BIT(1))
    LOCKGRANTED: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    LOCKEDBY: Mapped[Optional[str]] = mapped_column(String(255))


class IncomingMessage(Base):
    __tablename__ = 'incoming_message'

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    message_id: Mapped[str] = mapped_column(String(200))
    link_id: Mapped[str] = mapped_column(String(200))
    message: Mapped[str] = mapped_column(Text)
    short_code: Mapped[str] = mapped_column(String(50))
    phone_number: Mapped[str] = mapped_column(String(30))
    date_sent: Mapped[Optional[str]] = mapped_column(String(30))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))


class Migrations(Base):
    __tablename__ = 'migrations'

    id: Mapped[int] = mapped_column(INTEGER(10), primary_key=True)
    migration: Mapped[str] = mapped_column(String(255))
    batch: Mapped[int] = mapped_column(INTEGER(11))


class MobileNetwork(Base):
    __tablename__ = 'mobile_network'
    __table_args__ = (
        Index('mcc_ref', 'mcc_ref', unique=True),
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    country: Mapped[Optional[str]] = mapped_column(String(150))
    country_code: Mapped[Optional[str]] = mapped_column(String(5))
    mcc_code: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    mcc_ref: Mapped[Optional[int]] = mapped_column(BIGINT(20))
    mnc_code: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    network_name: Mapped[Optional[str]] = mapped_column(String(200))
    mobile_code: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))

    sms_outbox: Mapped[List['SmsOutbox']] = relationship('SmsOutbox', back_populates='mobile_network')


class NumberBlacklist(Base):
    __tablename__ = 'number_blacklist'

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String(150))
    sender_id: Mapped[Optional[str]] = mapped_column(String(15))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))


class OptOut(Base):
    __tablename__ = 'opt_out'

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    sender_id: Mapped[Optional[str]] = mapped_column(String(15))
    phone_number: Mapped[Optional[str]] = mapped_column(String(25))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))


class PasswordResetTokens(Base):
    __tablename__ = 'password_reset_tokens'

    email: Mapped[str] = mapped_column(String(255), primary_key=True)
    token: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)


class PersonalAccessTokens(Base):
    __tablename__ = 'personal_access_tokens'
    __table_args__ = (
        Index('personal_access_tokens_token_unique', 'token', unique=True),
        Index('personal_access_tokens_tokenable_type_tokenable_id_index', 'tokenable_type', 'tokenable_id')
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    tokenable_type: Mapped[str] = mapped_column(String(255))
    tokenable_id: Mapped[int] = mapped_column(BIGINT(20))
    name: Mapped[str] = mapped_column(String(255))
    token: Mapped[str] = mapped_column(String(64))
    abilities: Mapped[Optional[str]] = mapped_column(Text)
    last_used_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    expires_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)


class RemoteConfig(Base):
    __tablename__ = 'remote_config'
    __table_args__ = (
        Index('config-name-uk', 'app_name', 'config_name', unique=True),
        {'comment': 'Table to store remote configuration options'}
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    app_name: Mapped[str] = mapped_column(String(50))
    config_name: Mapped[str] = mapped_column(String(50))
    config_value: Mapped[str] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))


class UntrackedCallback(Base):
    __tablename__ = 'untracked_callback'
    __table_args__ = {'comment': 'Table to track unsaved callbacks'}

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    message_id: Mapped[str] = mapped_column(String(250), comment='message identifier')
    network_code: Mapped[Optional[str]] = mapped_column(String(50))
    phone_number: Mapped[Optional[str]] = mapped_column(String(100))
    message_status: Mapped[Optional[str]] = mapped_column(String(100))
    retry_count: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    failure_reason: Mapped[Optional[str]] = mapped_column(String(100))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        Index('user_email', 'email', unique=True),
        Index('user_name', 'username', unique=True),
        {'comment': 'Table to store account users'}
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    change_password: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    account_status: Mapped[str] = mapped_column(String(100), server_default=text("'ACTIVE'"))
    active: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    username: Mapped[Optional[str]] = mapped_column(String(18))
    email: Mapped[Optional[str]] = mapped_column(String(50))
    password: Mapped[Optional[str]] = mapped_column(String(200))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))

    user_api_account: Mapped[List['UserApiAccount']] = relationship('UserApiAccount', back_populates='user')
    user_tokens: Mapped[List['UserTokens']] = relationship('UserTokens', back_populates='users')


class ApiService(Base):
    __tablename__ = 'api_service'
    __table_args__ = (
        ForeignKeyConstraint(['user_uuid'], ['api_accounts.uuid'], onupdate='CASCADE', name='user_uid_fk'),
        Index('unique_user_sender_id', 'user_uuid', 'sender', 'type', 'service', unique=True),
        Index('unique_user_service', 'id', 'service', unique=True),
        Index('user_uid_fk', 'user_uuid')
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    user_uuid: Mapped[str] = mapped_column(String(64))
    service: Mapped[str] = mapped_column(String(20))
    active: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    type: Mapped[Optional[str]] = mapped_column(String(10), server_default=text("'BULK_SMS'"))
    sender: Mapped[Optional[str]] = mapped_column(String(11))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))

    api_accounts: Mapped['ApiAccounts'] = relationship('ApiAccounts', back_populates='api_service')


class ApiSmsCredit(Base):
    __tablename__ = 'api_sms_credit'
    __table_args__ = (
        ForeignKeyConstraint(['user_uuid'], ['api_accounts.uuid'], onupdate='CASCADE', name='user-credit-uid-fk'),
        Index('idx-credit-amount', 'credit_amount'),
        Index('user-credit-uid-fk', 'user_uuid'),
        {'comment': 'Table to track user SMS credit top ups'}
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    user_uuid: Mapped[str] = mapped_column(String(64))
    credit_amount: Mapped[decimal.Decimal] = mapped_column(DECIMAL(10, 2))
    remarks: Mapped[str] = mapped_column(String(150), comment='Comments regarding the top up')
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))

    api_accounts: Mapped['ApiAccounts'] = relationship('ApiAccounts', back_populates='api_sms_credit')


class FeeEndpoints(Base):
    __tablename__ = 'fee_endpoints'
    __table_args__ = (
        ForeignKeyConstraint(['username'], ['api_accounts.username'], name='fk-endpoint-username'),
        Index('uk-endpoint-username', 'username', unique=True)
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    username: Mapped[str] = mapped_column(String(18))
    data_endpoint: Mapped[str] = mapped_column(String(120))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))

    api_accounts: Mapped['ApiAccounts'] = relationship('ApiAccounts', back_populates='fee_endpoints')


class SmsCampaign(Base):
    __tablename__ = 'sms_campaign'
    __table_args__ = (
        ForeignKeyConstraint(['user_uuid'], ['api_accounts.uuid'], onupdate='CASCADE', name='user-campaign-uid-fk'),
        Index('idx-campaign-status', 'campaign_status'),
        Index('user-campaign-uid-fk', 'user_uuid')
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    user_uuid: Mapped[str] = mapped_column(String(64))
    campaign_name: Mapped[str] = mapped_column(String(255))
    is_draft: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    campaign_status: Mapped[Optional[str]] = mapped_column(String(100))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))

    api_accounts: Mapped['ApiAccounts'] = relationship('ApiAccounts', back_populates='sms_campaign')
    message_queue: Mapped[List['MessageQueue']] = relationship('MessageQueue', back_populates='campaign')


class SmsOutbox(Base):
    __tablename__ = 'sms_outbox'
    __table_args__ = (
        ForeignKeyConstraint(['network_code'], ['mobile_network.mcc_ref'], onupdate='CASCADE', name='fk_network_code'),
        Index('fk_network_code', 'network_code'),
        Index('idx-actual-cost', 'actual_cost'),
        Index('idx-created-at', 'created_at'),
        Index('idx-currency', 'currency'),
        Index('idx-delivery-status', 'delivery_status'),
        Index('idx-message-id', 'message_id'),
        Index('idx-sms-outbox-hash', 'message_hash'),
        Index('idx-sms-outbox-user-id', 'user_id')
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    archive_message: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    message_delivered: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    user_id: Mapped[Optional[int]] = mapped_column(BIGINT(20))
    campaign_id: Mapped[Optional[int]] = mapped_column(BIGINT(20))
    message_hash: Mapped[Optional[str]] = mapped_column(String(150))
    date_time: Mapped[Optional[str]] = mapped_column(String(100))
    message_id: Mapped[Optional[str]] = mapped_column(String(255))
    sender_id: Mapped[Optional[str]] = mapped_column(String(15))
    currency: Mapped[Optional[str]] = mapped_column(String(4))
    currency_rate: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2), server_default=text('0.00'))
    phone_number: Mapped[Optional[str]] = mapped_column(String(150))
    sms_text: Mapped[Optional[str]] = mapped_column(Text)
    network_code: Mapped[Optional[int]] = mapped_column(BIGINT(20), server_default=text('0'))
    character_count: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    sms_count: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    retry_count: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))
    single_sms_cost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    message_string_cost: Mapped[Optional[str]] = mapped_column(String(25))
    message_cost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    actual_cost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    delivery_status: Mapped[Optional[str]] = mapped_column(String(100))
    failure_reason: Mapped[Optional[str]] = mapped_column(String(100))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))

    mobile_network: Mapped['MobileNetwork'] = relationship('MobileNetwork', back_populates='sms_outbox')


class SmsStatistics(Base):
    __tablename__ = 'sms_statistics'
    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['api_accounts.id'], name='fk-sms-stats-user-id'),
        Index('fk-sms-stats-user-id', 'user_id'),
        Index('idx-message-date', 'message_date'),
        Index('idx-message-end-date', 'message_end_date'),
        Index('idx-message-start-date', 'message_start_date'),
        Index('idx-total-cost', 'total_cost'),
        Index('idx-total-messages', 'total_messages'),
        Index('idx-total-recipients', 'total_recipients'),
        {'comment': 'Table to store sms statistics'}
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    user_id: Mapped[int] = mapped_column(BIGINT(20))
    is_campaign: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    sender_id: Mapped[str] = mapped_column(String(11))
    total_recipients: Mapped[int] = mapped_column(BIGINT(20))
    total_cost: Mapped[decimal.Decimal] = mapped_column(DECIMAL(10, 2))
    total_messages: Mapped[int] = mapped_column(BIGINT(20))
    message_date: Mapped[datetime.date] = mapped_column(Date)
    message_start_date: Mapped[datetime.date] = mapped_column(Date)
    message_end_date: Mapped[datetime.date] = mapped_column(Date)

    user: Mapped['ApiAccounts'] = relationship('ApiAccounts', back_populates='sms_statistics')


class UserApiAccount(Base):
    __tablename__ = 'user_api_account'
    __table_args__ = (
        ForeignKeyConstraint(['account_id'], ['api_accounts.id'], ondelete='CASCADE', name='fk_api_account_api_id'),
        ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE', name='fk_api_account_user_id'),
        Index('fk_api_account_api_id', 'account_id'),
        Index('fk_user_id_account_id', 'user_id', 'account_id', unique=True),
        {'comment': 'Junction table for user accounts and api accounts for easier '
                'management'}
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    user_id: Mapped[Optional[int]] = mapped_column(BIGINT(20))
    account_id: Mapped[Optional[int]] = mapped_column(BIGINT(20))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))

    account: Mapped['ApiAccounts'] = relationship('ApiAccounts', back_populates='user_api_account')
    user: Mapped['Users'] = relationship('Users', back_populates='user_api_account')


class UserTokens(Base):
    __tablename__ = 'user_tokens'
    __table_args__ = (
        ForeignKeyConstraint(['user_name'], ['users.username'], ondelete='CASCADE', onupdate='CASCADE', name='fk_username_token'),
        Index('id', 'id', unique=True),
        Index('jwt_token_username', 'user_name'),
        Index('unique_jwt_token', 'token', unique=True)
    )

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    ip_address: Mapped[Optional[str]] = mapped_column(String(50))
    user_name: Mapped[Optional[str]] = mapped_column(String(18))
    token: Mapped[Optional[str]] = mapped_column(String(200))
    expiry_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))

    users: Mapped['Users'] = relationship('Users', back_populates='user_tokens')


class MessageQueue(Base):
    __tablename__ = 'message_queue'
    __table_args__ = (
        ForeignKeyConstraint(['campaign_id'], ['sms_campaign.id'], ondelete='CASCADE', onupdate='CASCADE', name='fk-campaign-id'),
        Index('fk-campaign-id', 'campaign_id'),
        Index('idx-message-queue-hash', 'message_hash'),
        Index('idx-phone-number', 'phone_number')
    )

    id: Mapped[int] = mapped_column(BIGINT(20), primary_key=True)
    campaign_id: Mapped[int] = mapped_column(BIGINT(20))
    message: Mapped[str] = mapped_column(Text)
    message_length: Mapped[int] = mapped_column(INTEGER(11), server_default=text('160'))
    number_valid: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    message_sent: Mapped[int] = mapped_column(TINYINT(1), server_default=text('1'))
    retry_count: Mapped[Optional[int]] = mapped_column(INTEGER(11), server_default=text('0'))
    message_hash: Mapped[Optional[str]] = mapped_column(String(150))
    message_status: Mapped[Optional[str]] = mapped_column(String(100))
    failure_reason: Mapped[Optional[str]] = mapped_column(String(100))
    phone_number: Mapped[Optional[str]] = mapped_column(String(150))
    sms_count: Mapped[Optional[int]] = mapped_column(INTEGER(11))
    message_cost: Mapped[Optional[decimal.Decimal]] = mapped_column(DECIMAL(10, 2))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('current_timestamp()'))

    campaign: Mapped['SmsCampaign'] = relationship('SmsCampaign', back_populates='message_queue')
