import AssignmentDetailPage from '../../../Components/AssignmentDetailPage';
import type { MemberAssignment } from '../../../types';

type SimulacroShowProps = {
    pageTitle: string;
    subtitle?: string;
    simulacro: MemberAssignment;
};

export default function SimulacroShow({ pageTitle, subtitle, simulacro }: SimulacroShowProps) {
    return (
        <AssignmentDetailPage
            pageTitle={pageTitle}
            subtitle={subtitle}
            assignment={simulacro}
            section="simulacros"
        />
    );
}
