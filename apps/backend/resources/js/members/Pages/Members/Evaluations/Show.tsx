import AssignmentDetailPage from '../../../Components/AssignmentDetailPage';
import type { MemberAssignment } from '../../../types';

type EvaluationShowProps = {
    pageTitle: string;
    subtitle?: string;
    evaluation: MemberAssignment;
};

export default function EvaluationShow({ pageTitle, subtitle, evaluation }: EvaluationShowProps) {
    return (
        <AssignmentDetailPage
            pageTitle={pageTitle}
            subtitle={subtitle}
            assignment={evaluation}
            section="evaluations"
        />
    );
}
