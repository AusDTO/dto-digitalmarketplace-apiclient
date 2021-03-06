from enum import Enum, unique


@unique
class AuditTypes(Enum):

    # User account events
    create_user = "create_user"
    update_user = "update_user"
    invite_user = "invite_user"
    user_auth_failed = "user_auth_failed"
    contact_update = "contact_update"
    supplier_update = "supplier_update"
    duplicate_supplier = "duplicate_supplier"

    # Draft service lifecycle event
    create_draft_service = "create_draft_service"
    update_draft_service = "update_draft_service"
    update_draft_service_status = "update_draft_service_status"
    complete_draft_service = "complete_draft_service"
    publish_draft_service = "publish_draft_service"
    delete_draft_service = "delete_draft_service"

    # Live service lifecycle events
    update_service = "update_service"
    import_service = "import_service"
    update_service_status = "update_service_status"

    # Brief lifecycle events
    create_brief = "create_brief"
    update_brief = "update_brief"
    update_brief_status = "update_brief_status"
    create_brief_response = "create_brief_response"
    read_brief_responses = "read_brief_responses"
    add_brief_clarification_question = "add_brief_clarification_question"
    delete_brief = "delete_brief"

    # Supplier actions
    register_framework_interest = "register_framework_interest"
    view_clarification_questions = "view_clarification_questions"
    send_clarification_question = "send_clarification_question"
    send_application_question = "send_application_question"
    answer_selection_questions = "answer_selection_questions"

    # Case Study lifecycle events
    create_casestudy = "create_casestudy"
    update_casestudy = "update_casestudy"
    delete_casestudy = "delete_casestudy"

    # Application lifecycle events
    create_application = "create_application"
    submit_application = "submit_application"
    revert_application = "revert_application"
    approve_application = "approve_application"
    reject_application = "reject_application"
    delete_application = "delete_application"

    create_assessment = "create_assessment"
    reject_assessment = "reject_assessment"

    unassessed_domain = "unassessed_domain"
    assessed_domain = "assessed_domain"

    feedback = "feedback"

    # Framework agreements
    upload_signed_agreement = "upload_signed_agreement"

    # Framework lifecycle
    create_framework = "create_framework"
    framework_update = "framework_update"

    # Admin actions
    upload_countersigned_agreement = "upload_countersigned_agreement"
    delete_countersigned_agreement = "delete_countersigned_agreement"
    snapshot_framework_stats = "snapshot_framework_stats"

    # Email actions
    send_seller_opportunities_campaign = "send_seller_opportunities_campaign"

    @staticmethod
    def is_valid_audit_type(test_audit_type):

        for name, audit_type in AuditTypes.__members__.items():
            if audit_type.value == test_audit_type:
                return True
        return False
